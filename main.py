import os
import json
from pathlib import Path
from flask import Flask, jsonify

app = Flask(__name__)

# Path to the directory containing JSON files
path = Path("json_files")

@app.route("/", methods=["GET"])
def get_recipes_from_json():
    if not path.exists():
        return "Directory Doesn't Exist", 404
    if not path.is_dir():
        return "Directory Doesn't Exist", 404
    
    all_data = []
    
    get_json_files = list(path.glob('**/*.json'))
    for file in get_json_files:
        try:
            with open(file, 'r') as json_files:
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
    
    return jsonify(all_data)
if __name__ == "__main__":
    app.run(debug=True)
