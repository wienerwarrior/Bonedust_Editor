import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import json_reader
from json_reader import JsonReader

window = ttk.Window(themename="darkly")
reader = JsonReader()

def list_json_files():
    file_list = reader.get_file_list()
    listbox.delete(0, END)  # Clear the current list
    for file in file_list:
        listbox.insert(END, file)

def select_folder():
    path = filedialog.askdirectory(title="Select Folder")
    if path:
        reader.set_directory(path)
        folder_path_label.config(text=path)
        list_json_files()
    return path

def create_recipe_json():
    try:
        recipe = {
            "RecipeID": int(id_entry.get()),
            "RecipeName": recipe_name_entry.get(),
            "GenerateName": bool(generate_name_bool.get()),
            "RequiredItems": [
                {
                    "ItemID": int(item_id_entry.get()),
                    "ItemAmount": int(item_amount_entry.get())
                }
            ],
            "HasRequiredItemTypes": bool(has_required_item_types_bool.get()),
            "RequiredItemTypes": None,
            "RecipeOutputItems": [
                {
                    "ItemID": int(item_id_entry.get()),
                    "ItemAmount": int(item_amount_entry.get())
                }
            ],
            "CraftedAt": ["Player"]
        }
        return recipe
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure all numerical fields are correctly filled.")
        return None

def save_recipe():
    recipe = create_recipe_json()
    if recipe:
        path = select_folder()
        if path:
            file_path = f"{path}/new_recipe.json"
            with open(file_path, 'w') as new_recipe:
                json.dump(recipe, new_recipe, indent=4)
            messagebox.showinfo("Recipe Saved", "Recipe has been saved successfully!")
            print(recipe)

if __name__ == "__main__":
    file_list = reader.get_file_list()
    json_data = reader.get_recipes_from_json()

# -----------------------------------------JSON UI ELEMENTS-----------------------------------------
ttk.Label(window, text="Recipe ID").grid(row=0, column=2, padx=10, pady=5, sticky="e")
id_entry = ttk.Entry(window)
id_entry.grid(row=0, column=3, padx=10, pady=5, sticky="w")

ttk.Label(window, text="Recipe Name").grid(row=1, column=2, padx=10, pady=5, sticky="e")
recipe_name_entry = ttk.Entry(window)
recipe_name_entry.grid(row=1, column=3, padx=10, pady=5, sticky="w")

ttk.Label(window, text="Generate Name").grid(row=2, column=2, padx=10, pady=5, sticky="e")
generate_name_bool = ttk.Combobox(values=["true", "false"])
generate_name_bool.grid(row=2, column=3, padx=10, pady=5, sticky="e")

ttk.Label(window, text="Item ID").grid(row=3, column=2, padx=10, pady=5, sticky="e")
item_id_entry = ttk.Entry(window)
item_id_entry.grid(row=3, column=3, padx=10, pady=5, sticky="w")

ttk.Label(window, text="Item Amount").grid(row=4, column=2, padx=10, pady=5, sticky="e")
item_amount_entry = ttk.Entry(window)
item_amount_entry.grid(row=4, column=3, padx=10, pady=5, sticky="w")

ttk.Label(window, text="Has Required Item Types").grid(row=5, column=2, padx=10, pady=5, sticky="e")
has_required_item_types_bool = ttk.Combobox(values=["true", "false"])
has_required_item_types_bool.grid(row=5, column=3, padx=10, pady=5, sticky="e")

ttk.Label(window, text="Required Item Type").grid(row=6, column=2, padx=10, pady=5, sticky="e")
item_type_entry = ttk.Entry(window)
item_type_entry.grid(row=6, column=3, padx=10, pady=5, sticky="w")

ttk.Label(window, text="Required Item Amount").grid(row=7, column=2, padx=10, pady=5, sticky="e")
required_item_amount_entry = ttk.Entry(window)
required_item_amount_entry.grid(row=7, column=3, padx=10, pady=5, sticky="w")

# -----------------------------------------UI ELEMENTS-----------------------------------------
folder_path_label = ttk.Label(window, text="No folder selected", wraplength=300)
folder_path_label.grid(column=0, row=0, columnspan=4, padx=10, pady=10, sticky="nw")

file_list_frame = ttk.Frame(window)
file_list_frame.grid(column=0, row=1, rowspan=7, padx=10, pady=10, sticky="nsew")

listbox = tk.Listbox(file_list_frame, selectmode=tk.SINGLE, width=50, height=20)
listbox.grid(column=0, row=0, padx=10, pady=10, sticky="nsew")

# Create a scrollbar for the Listbox
scrollbar = ttk.Scrollbar(file_list_frame, orient="vertical", command=listbox.yview)
scrollbar.grid(column=1, row=0, sticky="ns")

listbox.config(yscrollcommand=scrollbar.set)

# -----------------------------------------BUTTON ELEMENTS-----------------------------------------
save_btn = ttk.Button(window, text="Save", command=save_recipe, bootstyle=SUCCESS)
save_btn.grid(column=1, row=1, padx=10, pady=10, sticky="sw")

load_btn = ttk.Button(window, text="Load", command=select_folder, bootstyle=SUCCESS)
load_btn.grid(column=1, row=2, padx=10, pady=10, sticky="sw")

select_folder_btn = ttk.Button(window, text="Select Folder", command=select_folder, bootstyle=SUCCESS)
select_folder_btn.grid(column=1, row=3, padx=10, pady=10, sticky="sw")

# Configure grid weights for resizing
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
file_list_frame.grid_rowconfigure(0, weight=1)
file_list_frame.grid_columnconfigure(0, weight=1)

window.mainloop()
