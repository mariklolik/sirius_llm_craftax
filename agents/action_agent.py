from agents.sdk import sdk

class ActionAgent:
    def __init__(self):
        model = sdk.models.completions("yandexgpt")
        self.model = model.configure(temperature=0.0)

    def generate_code(self, task, code, errors, critique, skills):
        with open("action_template_system_promt") as file:
            action_template_system_promt = file.read()
        with open("action_template") as file:
            action_template = file.read()

        action_template.format(task, code, errors, critique, skills)

        result = self.model.run([
            {
                "role": "system",
                "text": action_template_system_promt,
            },
            {
                "role": "user",
                "text": action_template,
            }
        ])

        return result.alternatives[0].text.split('\n')
    