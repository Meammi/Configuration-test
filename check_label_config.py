from label_studio_sdk import LabelStudio
from dotenv import dotenv_values
import requests

key = dotenv_values(".env")

LABEL_STUDIO_URL = 'http://localhost:8080'
API_KEY = key["API_KEY"]
project_id = '14'
ls = LabelStudio(base_url=LABEL_STUDIO_URL, api_key=API_KEY)

with open("config.xml") as f:
    label_config_patch = f.read()



# Patch Config
project = ls.projects.update(
    title='Dental test',
    id = project_id,
    label_config= label_config_patch,
)


# print(project.title)
# print(project.description)
# print(project.label_config)
