from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
import os
from vault_manager import VaultManager

VAULT_MANAGER = VaultManager()

def create_vault(vault_name):
    # Create the vault
    VAULT_MANAGER.create_vault(vault_name)

    print(f"Vault '{vault_name}' created.")

def delete_vault(vault_name):
    confirm = input(f"Are you sure you want to delete vault '{vault_name}'? (y/n): ")
    if confirm.lower() == 'y':
        VAULT_MANAGER.delete_vault(vault_name)
        print(f"Vault '{vault_name}' deleted.")
    else:
        print("Operation cancelled.")

def list_variables(vault):
    # Load the vault
    vault = VAULT_MANAGER.load_vault(vault)

    # List the variables in the vault
    variables = vault.list_variables()

    # Print the variables
    for variable in variables:
        print(variable)

def list_vaults():
    vaults = VAULT_MANAGER.list_vaults()

    # Print the vaults
    for vault in vaults:
        print(vault)

def add_variable(vault_name):
    # Get all environment variables
    env_vars = os.environ.keys()

    # Create a completer with the environment variables
    env_var_completer = FuzzyWordCompleter(env_vars)

    # Load the vault
    vault = VAULT_MANAGER.load_vault(vault_name)

    # Prompt the user to select an environment variable
    while True:
        selected_var = prompt("Enter and select an environment variable (or type 'done' to finish): ", completer=env_var_completer)
        if selected_var.lower() == 'done':
            VAULT_MANAGER.save_vaults()
            break
        elif selected_var in env_vars:
            # Add the selected variable to the vault
            vault.add_variable(selected_var)
        else:
            print("Invalid selection. Please select a valid environment variable.")

    print(f"Added selected variables to vault '{vault_name}'. The vault now contains:")
    for var in vault.variables:
        print(var)

def delete_variable(vault_name, variable_name):
    # Load the vault
    vault = VAULT_MANAGER.load_vault(vault_name)

    # Prompt the user for confirmation
    confirm = input(f"Are you sure you want to delete variable '{variable_name}' from vault '{vault_name}'? (y/n): ")
    if confirm.lower() == 'y':
        # Delete the variable
        vault.delete_variable(variable_name)

        # Save the vault
        VAULT_MANAGER.save_vault(vault)

        print(f"Variable '{variable_name}' deleted from vault '{vault_name}'.")
    else:
        print("Operation cancelled.")