import argparse
from label_studio_sdk import LabelStudio
from dotenv import dotenv_values

#Load Config
key = dotenv_values(".env")
api_key = key["API_KEY"]
LABEL_STUDIO_URL = key["LABEL_STUDIO_URL"]

#Connect to Label Studio
ls = LabelStudio(base_url=LABEL_STUDIO_URL, api_key=api_key)

def list_projects():
    projects = ls.projects.list()
    for project in projects:
        print(f"ID: {project.id} | Title: {project.title}")
    return

def show_config(project_id):
    try:
        project = ls.projects.get(project_id)
        print("Label Configuration:\n")
        print(project.label_config)
    except Exception as e:
        print(f"Error: {e}")

def show_info(project_id):
    try:
        project = ls.projects.get(project_id)
        print(f"Project ID: {project.id}")
        print(f"Title: {project.title}")
        print(f"Description: {project.description}")
        print(f"Created By: {project.created_by}")
        print(f"Created At: {project.created_at}")
        print(f"Image amount: {project.queue_total}")
    except Exception as e:
        print(f"Error: {e}")
        
def show_global_config():
    try:
        with open("config.xml") as f:
            label_global_config = f.read()
        print(label_global_config)
        f.close()
    except Exception as e:
        print(f"Error: {e}")

def update_config(project_ids):
    try:
        with open("config.xml") as f:
            label_global_config = f.read()

        for project_id in project_ids:
            try:
                ls.projects.update(
                    id=project_id,
                    label_config=label_global_config
                )
                print(f"Updated config for project ID {project_id}")
            except Exception as e:
                print(f"Failed to update project {project_id}: {e}")

    except FileNotFoundError:
        print("config.xml not found.")
    except Exception as e:
        print(f"Error reading config: {e}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Label Studio projects")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List all Label Studio projects")

    config_parser = subparsers.add_parser("config", help="Show label config for a project")
    config_parser.add_argument("project_id", type=int, help="ID of the project")

    info_parser = subparsers.add_parser("info", help="Show detailed info about a project")
    info_parser.add_argument("project_id", type=int, help="ID of the project")

    subparsers.add_parser("globalconfig", help="Show global label config")

    update_parser = subparsers.add_parser("update-config", help="Update config for one or more projects")
    update_parser.add_argument("project_ids", nargs="+", type=int, help="List of project IDs to update")

    args = parser.parse_args()

    if args.command == "list":
        list_projects()
    elif args.command == "config":
        show_config(args.project_id)
    elif args.command == "info":
        show_info(args.project_id)
    elif args.command == "globalconfig":
        show_global_config()
    elif args.command == "update-config":
        update_config(args.project_ids)
    else:
        parser.print_help()
