from agents.sdk import sdk
from agents.formating import format_text_with_state
import json

class CriticAgent:
    def __init__(self):
        model = sdk.models.completions("yandexgpt")
        self.model = model.configure(temperature=0.0)

    def check_task_success(self, state, task, context):
        with open("system_promts/critic.txt") as file:
            critic_system_promt = file.read()

        with open("user_promts/critic.txt") as file:
            critic_user_promt = file.read()

        critic_user_promt = format_text_with_state(critic_user_promt, state, task, context)

        result = self.model.run(
            [
                {
                    "role": "system",
                    "text": critic_system_promt,
                },
                {
                    "role": "user",
                    "text": critic_user_promt,
                },
            ]
        )
        data = json.loads(result.alternatives[0].text.replace("```", ''))

        return bool(data['success']), data['critique']
