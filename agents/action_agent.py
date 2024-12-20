from agents.sdk import sdk
from agents.formating import format_text_with_state
import json

class ActionAgent:
    def __init__(self):
        model = sdk.models.completions("yandexgpt-32k")
        self.model = model.configure(temperature=0.0)

    def generate_code(self, code, error, state, task, context, critique):
        with open("system_promts/action_template.txt") as file:
            action_template_system_promt = file.read()
        with open("system_promts/action_response_format.txt") as file:
            action_template_system_promt += file.read()

        with open("user_promts/action.txt") as file:
            action = file.read()

        action = format_text_with_state(action, state, code, error, task, context, critique)

        result = self.model.run(
            [
                {
                    "role": "system",
                    "text": action_template_system_promt,
                },
                {
                    "role": "user",
                    "text": action,
                },
            ]
        )
        data = result.alternatives[0].text.replace("```", '')
        
        
        return data
