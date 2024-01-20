import argparse
import cli

def main():
    parser = argparse.ArgumentParser(description='Manage environment variable vaults.')
    subparsers = parser.add_subparsers(dest='command')

    # Define the 'create' command
    create_parser = subparsers.add_parser('create', help='Create a new vault')
    create_parser.add_argument('name', help='The name of the vault to create')

    # Define the 'delete' command
    delete_parser = subparsers.add_parser('delete', help='Delete a vault')
    delete_parser.add_argument('name', help='The name of the vault to delete')

    # Define the 'list' command
    list_parser = subparsers.add_parser('list', help='List all vaults')

    # Define the 'add' command
    add_parser = subparsers.add_parser('add', help='Add a variable to a vault')
    add_parser.add_argument('vault', help='The name of the vault')
    add_parser.add_argument('variable', help='The name of the variable')

    # Define the 'delete-var' command
    delete_var_parser = subparsers.add_parser('delete-var', help='Delete a variable from a vault')
    delete_var_parser.add_argument('vault', help='The name of the vault')
    delete_var_parser.add_argument('variable', help='The name of the variable')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the appropriate function based on the command
    if args.command == 'create':
        cli.create_vault(args.name)
    elif args.command == 'delete':
        cli.delete_vault(args.name)
    elif args.command == 'list':
        cli.list_vaults()
    elif args.command == 'add':
        cli.add_variable(args.vault, args.variable)
    elif args.command == 'delete-var':
        cli.delete_variable(args.vault, args.variable)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()