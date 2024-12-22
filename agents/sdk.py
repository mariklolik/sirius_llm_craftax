from yandex_cloud_ml_sdk import YCloudML
from dotenv import load_dotenv
from os import environ

import os
import datetime

load_dotenv()


sdk = YCloudML(folder_id=environ["folder_id"], auth=environ["auth"])

class Run:
    def __init__(self):
        self.base_directory = "logs_promts"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.directory = os.path.join(self.base_directory, f"Run_{current_time}")
        os.makedirs(self.directory, exist_ok=True)

    def run(self, model, promt):
        file_name = f"promt_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        file_path = os.path.join(self.directory, file_name)

        result = model.run(promt)
        with open(file_path, 'w') as file:
            file.write(promt)
            file.write("\n\nResult:\n")
            file.write(result.alternatives[0].text)
        
        return result


