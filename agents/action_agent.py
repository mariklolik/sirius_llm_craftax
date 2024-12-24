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
        with open(
            "system_promts/action_template.txt", encoding="utf-8"
        ) as file:
            self.action_template_system_promt = file.read()
        with open(
            "system_promts/action_response_format.txt", encoding="utf-8"
        ) as file:
            self.action_template_system_promt += file.read()
        with open(
            "user_promts/action_user_promt.txt", encoding="utf-8"
        ) as file:
            self.action = file.read()

    def generate_code(
        self, code, error, state, task, context, critique, env_fid
    ):

        action = format_text_with_state(
            self.action, state, code, error, task, context, critique, env_fid
        )

        result = self.logs_run.run(
            self.model,
            [
                {
                    "role": "system",
                    "text": self.action_template_system_promt,
                },
                {
                    "role": "user",
                    "text": action,
                },
            ],
        )
        data = result.alternatives[0].text.replace("```", "")

        return data
