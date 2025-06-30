from label_studio_sdk import LabelStudio
from dotenv import dotenv_values

def update_label_config(project_id: str, LABEL_STUDIO_URL: str , config_path: str):
  key = dotenv_values(".env")
  api_key = key["API_KEY"]

  ls = LabelStudio(base_url=LABEL_STUDIO_URL, api_key=api_key)
  with open(config_path) as f:
    label_config_patch = f.read()
    
  project = ls.projects.update(
    id=project_id,
    label_config=label_config_patch,
  )
  return project

