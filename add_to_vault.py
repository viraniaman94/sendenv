import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter

# A dictionary to represent the vaults
vaults = {}

def add_to_vault(vault_name):
    # Get all environment variables
    env_vars = os.environ.keys()

    # Create a completer with the environment variables
    env_var_completer = FuzzyWordCompleter(env_vars)

    # Prompt the user to select an environment variable
    while True:
        selected_var = prompt("Select an environment variable (or type 'done' to finish): ", completer=env_var_completer)
        if selected_var.lower() == 'done':
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

# Example usage
add_to_vault('myVault')