from yandex_cloud_ml_sdk import YCloudML
from dotenv import load_dotenv
from os import environ
load_dotenv()

sdk = YCloudML(folder_id=environ("folder_id"), auth=environ("auth"))