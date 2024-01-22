from prompt_toolkit import prompt
from prompt_toolkit.completion import FuzzyWordCompleter
import os
from vault_manager import VaultManager
from twisted.internet import reactor, defer
from wormhole import create
from wormhole.cli.public_relay import MAILBOX_RELAY
import json


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

@defer.inlineCallbacks
def send_vault_async(vault_name):
    vault = VAULT_MANAGER.load_vault(vault_name)
    if not vault:
        print(f"Vault {vault_name} does not exist.")
        return

    w = yield create("magicenv.dev", MAILBOX_RELAY, reactor)
    yield w.allocate_code()

    code = yield w.get_code()
    print(f"code: {code}")

    data = {
        "vault": vault_name,
        "variables": vault.variables
    }

    yield w.send_message(json.dumps(data).encode('utf-8'))

    # Wait for an acknowledgement from the receiver
    ack = yield w.get_message()
    print(f"Acknowledgement received: {ack}")

    yield w.close()
    reactor.stop()

@defer.inlineCallbacks
def receive_vault_async():
    w = yield create("magicenv.dev", MAILBOX_RELAY, reactor)

    # Set the code for the wormhole
    print("Enter the code: ")
    code = input()
    yield w.set_code(code)

    # Receive the message
    message = yield w.get_message()
    data = json.loads(message.decode('utf-8'))
    print(f"Received data: {data}")

    # Save the received vault
    vault_name = data['vault']
    variables = data['variables']
    create_vault(vault_name)

    for variable in variables:
        add_variable(vault_name, variable)

    # Send an acknowledgement back to the sender
    yield w.send_message(b"Received")

    # Close the wormhole
    yield w.close()
    reactor.stop()

def send_vault(vault_name):
    reactor.callWhenRunning(send_vault_async, vault_name)
    reactor.run()

def receive_vault():
    reactor.callWhenRunning(receive_vault_async)
    reactor.run()