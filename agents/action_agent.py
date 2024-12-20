from agents.sdk import sdk
from agents.formating import format_text_with_state


class ActionAgent:
    def __init__(self):
        model = sdk.models.completions("yandexgpt")
        self.model = model.configure(temperature=0.0)

    def generate_code(self, code, error, state, task, context, critique):
        with open("system_promts/action_template.txt") as file:
            action_template_system_promt = file.read()
        with open("system_promts/action_response_format.txt") as file:
            action_template_system_promt += file.read()

        with open("user_promts/action.txt") as file:
            action = file.read()

        action = action.format(code, error)
        action = format_text_with_state(action, state)
        action = action.format(task, context, critique)

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

        return result.alternatives[0].text.split("\n")
