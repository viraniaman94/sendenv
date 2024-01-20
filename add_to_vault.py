import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
import os
import json

# Read the vaults from the file
vaults_file_path = os.path.expanduser("~/.magicenv/config.json")
if os.path.exists(vaults_file_path):
    with open(vaults_file_path, "r") as f:
        vaults = json.load(f)
else:
    vaults = {}

def add_to_vault(vault_name):
    # Get all environment variables
    env_vars = os.environ.keys()

    # Create a completer with the environment variables
    env_var_completer = FuzzyWordCompleter(env_vars)

    # Prompt the user to select an environment variable
    while True:
        selected_var = prompt("Enter and select an environment variable (or type 'done' to finish): ", completer=env_var_completer)
        if selected_var.lower() == 'done':
            # Save the updated vaults to the file
            with open(vaults_file_path, "w") as f:
                json.dump(vaults, f)
            break
        elif selected_var in env_vars:
            # Add the selected variable to the vault
            if vault_name not in vaults:
                vaults[vault_name] = []
            vaults[vault_name].append({selected_var: os.environ[selected_var]})
        else:
            print("Invalid selection. Please select a valid environment variable.")

    print(f"Added selected variables to vault '{vault_name}'. The vault now contains:")
    for var in vaults[vault_name]:
        print(var)