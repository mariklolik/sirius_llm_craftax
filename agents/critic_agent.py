from agents.sdk import sdk
from agents.formating import format_text_with_state
import json

class CriticAgent:
    def __init__(self, logs_run):
        model = sdk.models.completions("yandexgpt")
        self.model = model.configure(temperature=0.0)
        self.logs_run = logs_run
        with open("system_promts/tutorial_with_constants.txt", encoding="utf-8") as file:
            self.tutorial = file.read()
        with open("system_promts/critic.txt") as file:
            self.critic_system_promt = file.read()
        with open("user_promts/critic.txt") as file:
            self.critic_user_promt = file.read()

    def check_task_success(self, state, task, context):

        critic_user_promt = format_text_with_state(self.critic_user_promt, state, task, context)

        result = self.logs_run.run(self.model, 
            [
                {
                    "role": "system",
                    "text": self.tutorial + self.critic_system_promt,
                },
                {
                    "role": "user",
                    "text": critic_user_promt,
                },
            ]
        )
        data = json.loads(result.alternatives[0].text.replace("```", ''))
        return data['reasoning'], data['success'], data['critique']
