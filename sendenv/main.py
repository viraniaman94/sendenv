import argparse
import json
import os
import cli as cli
from config import VAULTS_CONFIG, VAULTS_STORAGE

def main():
    parser = argparse.ArgumentParser(description='Manage environment variable vaults.')
    subparsers = parser.add_subparsers(dest='command')

    # Define the 'create' command
    create_parser = subparsers.add_parser('create-vault', help='Create a new vault')
    create_parser.add_argument('name', help='The name of the vault to create')

    # Define the 'delete' command
    delete_parser = subparsers.add_parser('delete-vault', help='Delete a vault')
    delete_parser.add_argument('name', help='The name of the vault to delete')

    # Define the 'list' command
    list_parser = subparsers.add_parser('list-vaults', help='List all vaults')

    # Define the 'add' command
    add_parser = subparsers.add_parser('add-var', help='Add a variable to a vault. If no variable is provided, the user will be prompted to select one.')
    add_parser.add_argument('vault', help='The name of the vault')
    add_parser.add_argument('variable', nargs='?', default=None, help='The name of the variable')

    # Define the 'delete-var' command
    delete_var_parser = subparsers.add_parser('delete-var', help='Delete a variable from a vault. If no variable is provided, the user will be prompted to select one.')
    delete_var_parser.add_argument('vault', help='The name of the vault')
    delete_var_parser.add_argument('variable', nargs='?', default=None, help='The name of the variable')

    # Define the 'send' command
    send_parser = subparsers.add_parser('send-vault', help='Send a vault to a remote server')
    send_parser.add_argument('vault', help='The name of the vault to send')

    # Define the 'receive' command
    receive_parser = subparsers.add_parser('receive-vault', help='Receive a vault from a remote server')

    # Define the 'list-var' command
    list_var_parser = subparsers.add_parser('list-var', help='List all variables in a vault')
    list_var_parser.add_argument('vault', help='The name of the vault')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the command
    if args.command == 'create-vault':
        cli.create_vault(args.name)
    elif args.command == 'delete-vault':
        cli.delete_vault(args.name)
    elif args.command == 'list-vaults':
        cli.list_vaults()
    elif args.command == 'add-var':
        cli.add_variable(args.vault, args.variable)
    elif args.command == 'delete-var':
        cli.delete_variable(args.vault, args.variable)
    elif args.command == 'list-var':
        cli.list_variables(args.vault)
    elif args.command == 'send-vault':
        cli.send_vault(args.vault)
    elif args.command == 'receive-vault':
        cli.receive_vault()
    else:
        parser.print_help()

def initialize_files():
    files = [VAULTS_CONFIG, VAULTS_STORAGE]
    for file in files:
        file = os.path.expanduser(file)
        if not os.path.exists(file):
            dir = os.path.dirname(file)
            if not os.path.exists(dir):
                os.makedirs(dir)
            with open(file, 'w') as f:
                json.dump({}, f)

if __name__ == '__main__':
    initialize_files()
    main()