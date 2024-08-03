import os
import json
from pathlib import Path


class JsonReader:
    def __init__(self):
        # Path to the directory containing JSON files
        self.path = Path("")

    def set_directory(self, directory):
        self.path = Path(directory)
    def get_file_list(self):
        if not self.path.exists():
            return "Directory Doesn't Exist"
        if not self.path.is_dir():
            return "Directory Doesn't Exist"

        files_from_dir = [file for file in os.listdir(self.path) if os.path.isfile(self.path / file)]
        return files_from_dir

    def get_recipes_from_json(self):
        if not self.path.exists():
            return "Directory Doesn't Exist"
        if not self.path.is_dir():
            return "Directory Doesn't Exist"

        all_data = []
        get_json_files = list(self.path.glob("**/*.json"))
        for file in get_json_files:
            try:
                with open(file, "r") as json_files:
                    # Check if the file is empty
                    if json_files.read(1):
                        json_files.seek(0)  # Go back to the start of the file
                        data = json.load(json_files)
                        all_data.append(data)
                    else:
                        print(f"Skipping empty file: {file}")
            except json.JSONDecodeError as error:
                print(f"Error decoding JSON from file {file}: {error}")
            except Exception as error:
                print(f"Error reading file {file}: {error}")
        return all_data
