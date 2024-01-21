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

def add_variable(vault_name, variable_name=None):
    # Load the vault
    vault = VAULT_MANAGER.load_vault(vault_name)

    if variable_name:
        # If a variable name was provided, add it to the vault
        vault.add_variable(variable_name)
        print(f"Added variable '{variable_name}' to vault '{vault_name}'.")
    else:
        # If no variable name was provided, prompt the user to add names
        # Get all environment variables
        env_vars = list(os.environ.keys())

        # Create a completer with the environment variables
        env_var_completer = FuzzyWordCompleter(env_vars)

        # Prompt the user to select an environment variable
        while True:
            selected_var = prompt("Enter and select an environment variable (or type 'done' to finish): ", completer=env_var_completer)
            if selected_var.lower() == 'done':
                VAULT_MANAGER.save_vaults()
                break
            elif selected_var in env_vars:
                # Add the selected variable to the vault
                vault.add_variable(selected_var)
                env_vars.remove(selected_var)
            else:
                print("Invalid selection. Please select a valid environment variable.")

        print(f"Added selected variables to vault '{vault_name}'. The vault now contains:")
        for var in vault.variables:
            print(var)

def delete_variable(vault_name, variable_name=None):
    # Load the vault
    vault = VAULT_MANAGER.load_vault(vault_name)

    if variable_name:
        # If a variable name was provided, delete it from the vault
        vault.delete_variable(variable_name)
        print(f"Deleted variable '{variable_name}' from vault '{vault_name}'.")
    else:
        # If no variable name was provided, prompt the user to delete names
        # Get all variables in the vault
        vault_vars = vault.variables

        # Create a completer with the vault variables
        vault_var_completer = FuzzyWordCompleter(vault_vars)

        # Prompt the user to select a variable to delete
        while True:
            selected_var = prompt("Enter and select a variable to delete (or type 'done' to finish): ", completer=vault_var_completer)
            if selected_var.lower() == 'done':
                VAULT_MANAGER.save_vaults()
                break
            elif selected_var in vault_vars:
                # Delete the selected variable from the vault
                vault.delete_variable(selected_var)
            else:
                print("Invalid selection. Please select a valid variable.")

        print(f"Deleted selected variables from vault '{vault_name}'. The vault now contains:")
        for var in vault.variables:
            print(var)