from agents.sdk import sdk
from agents.formating import format_text_with_state
import json
import logging
logger = logging.getLogger("ActionAgent")

class ActionAgent:
    def __init__(self, logs_run):
        model = sdk.models.completions("yandexgpt-32k")
        self.model = model.configure(temperature=0.0)
        self.logs_run = logs_run
        with open("system_promts/tuturial_with_constans.txt") as file:
            self.tutorial = file.read()
        with open("system_promts/action_template.txt") as file:
            self.action_template_system_promt = file.read()
        with open("system_promts/action_response_format.txt") as file:
            self.action_template_system_promt += file.read()
        with open("user_promts/action.txt") as file:
            self.action = file.read()

    def generate_code(self, code, error, state, task, context, critique):

        action = format_text_with_state(self.action, state, code, error, task, context, critique)

        result = self.logs_run.run(self.model, 
            [
                {
                    "role": "system",
                    "text": self.tutorial + self.action_template_system_promt,
                },
                {
                    "role": "user",
                    "text": action,
                },
            ]
        )
        data = result.alternatives[0].text.replace("```", '')
        
        
        return data
