from agents.sdk import sdk

class CurriculumAgent:
    def __init__(self):
        model = sdk.models.completions("yandexgpt")
        self.model = model.configure(temperature=0.0)
        self.completed_tasks = []
        self.failed_tasks = []


    def get_exploration_progress(self, state):

        with open("qa_step_1_system_promt") as file:
            qa_step_1_promt_system_promt = file.read()
        with open("qa_step_1") as file:
            qa_step_1_promt = file.read()

        user_promt = qa_step_1_promt.format(self.completed_tasks, self.failed_tasks, state)

        result = self.model.run([
            {
                "role": "system",
                "text": qa_step_1_promt_system_promt,
            },
            {
                "role": "user",
                "text": user_promt,
            }
        ])

        result = result.alternatives[0].text.split('\n')
        reasoning = result[0]
        questions = []
        concepts = []
        for num, i in enumerate(result[1:]):
            if num % 2  == 0:
                questions.append(i)
            else:
                concepts.append(i)
        
        with open("qa_step_2_system_promt") as file:
            qa_step_2_promt_system_promt = file.read()
        with open("qa_step_2") as file:
            qa_step_2_promt = file.read()

        exploration_progress = []

        for question in questions:
            user_promt = qa_step_2_promt.format(question)
            
            result = self.model.run([
                {
                    "role": "system",
                    "text": qa_step_2_promt_system_promt,
                },
                {
                    "role": "user",
                    "text": user_promt,
                }
            ])

            answer = result.alternatives[0].text.split('\n')
            exploration_progress.append(
                {
                    "question": question,
                    "answer": answer
                }
            )
        return exploration_progress
    
    def propose_next_task(self, state, exploration_progress):
        with open("curriculum_system_promt") as file:
            curriculum_system_promt = file.read()
        with open("curriculum_user_promt") as file:
            curriculum_user_promt = file.read()
        for ques_and_answ in exploration_progress:
            curriculum_user_promt.format(ques_and_answ['question'], ques_and_answ['answer'])
        result = self.model.run([
            {
                "role": "system",
                "text": curriculum_system_promt,
            },
            {
                "role": "user",
                "text": curriculum_user_promt,
            }
        ])
        answer = result.alternatives[0].text.split('\n')
        reasoning = answer[0]
        task = answer[1] 
        return reasoning, task 


    def add_completed_tasks(self, task):
        self.completed_tasks.append(task)
    
    def add_failed_tasks(self, task):
        self.failed_tasks.append(task)