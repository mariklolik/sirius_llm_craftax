from agents.sdk import sdk
from agents.formating import format_text_with_state


class CurriculumAgent:
    def __init__(self, logs_run):
        model = sdk.models.completions("yandexgpt-32k")
        model.configure(temperature=0.0)
        self.model = model
        self.completed_tasks = []
        self.failed_tasks = []
        self.logs_run = logs_run
        with open("system_promts/tutorial.txt", encoding="utf-8") as file:
            self.tutorial = file.read()
        with open("system_promts/curriculum_qa_step1_ask_questions.txt") as file:
            self.qa_step_1_promt_system_promt = file.read()
        with open("user_promts/curriculum_qa_step1.txt") as file:
            self.qa_step_1_promt = file.read()

        with open("system_promts/curriculum_qa_step2_answer_questions.txt") as file:
            self.qa_step_2_promt_system_promt = file.read()
        with open("user_promts/curriculum_qa_step2.txt") as file:
            self.qa_step_2_promt = file.read()

        with open("system_promts/curriculum.txt") as file:
            self.curriculum_system_promt = file.read()
        with open("user_promts/curriculum.txt") as file:
            self.curriculum_user_promt = file.read()
        
        with open("system_promts/curriculum_task_decomposition.txt") as file:
            self.task_decomp_system_promt = file.read()
        with open("user_promts/curriculum_task_decomposition.txt") as file:
            self.task_decomp_user_promt = file.read()

    def get_exploration_progress(self, state):

        user_promt = format_text_with_state(self.qa_step_1_promt, state, self.completed_tasks, self.failed_tasks)

        result = self.logs_run.run(self.model,
            [
                {
                    "role": "system",
                    "text": self.tutorial + self.qa_step_1_promt_system_promt,
                },
                {
                    "role": "user",
                    "text": user_promt,
                },
            ]
        )
        result = result.alternatives[0].text.split("\n")
        result = [i for i in result if i]
        reasoning = result[0]
        questions = []
        concepts = []
        for num, i in enumerate(result[1:]):
            if num % 2 == 0:
                questions.append(i)
            else:
                concepts.append(i)

        exploration_progress = []

        for i in range(len(questions)):
            user_promt = self.qa_step_2_promt.format(questions[i], concepts[i])

            result = self.logs_run.run(self.model,
                [
                    {
                        "role": "system",
                        "text": self.tutorial + self.qa_step_2_promt_system_promt,
                    },
                    {
                        "role": "user",
                        "text": user_promt,
                    },
                ]
            )

            answer = result.alternatives[0].text
            exploration_progress.append(
                {"question": questions[i], "answer": answer}
            )
        return exploration_progress

    def propose_next_task(self, state, exploration_progress):
        curriculum_user_promt = format_text_with_state(
            self.curriculum_user_promt, state, self.completed_tasks, self.failed_tasks
        )

        start_promt = ""
        for ques_and_answ in exploration_progress:
            start_promt += f"Question: {ques_and_answ['question']}\nAnswer: {ques_and_answ['answer']}"
        user_promt = start_promt + curriculum_user_promt
        result = self.logs_run.run(self.model,
            [
                {
                    "role": "system",
                    "text": self.tutorial + self.curriculum_system_promt,
                },
                {
                    "role": "user",
                    "text": user_promt,
                },
            ]
        )
        answer = result.alternatives[0].text.split("\n")
        reasoning = answer[0]
        task = answer[1]
        return reasoning, task

    def task_decomposition(self, state, task):

        task_decomp_user_promt = self.task_decomp_user_promt.format(
            state.inventory, task
        )

        result = self.logs_run.run(self.model,
            [
                {
                    "role": "system",
                    "text": self.tutorial + self.task_decomp_system_promt,
                },
                {
                    "role": "user",
                    "text": task_decomp_user_promt,
                },
            ]
        )
        answer = result.alternatives[0].text
        
        answer = answer[answer.find("["):answer.rfind("]") + 1]
        return eval(answer)

    def add_completed_task(self, task):
        self.completed_tasks.append(task)

    def add_failed_task(self, task):
        self.failed_tasks.append(task)
