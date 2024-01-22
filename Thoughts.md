Thoughts

Tool that allows people to securely share environmental variables from one user to another, using magic-wormhole. 

Features: We discussed several potential features for your tool, including Vault Versioning, Environment Profiles, Integration with Other Tools, and Teams. We decided to focus on the core features first, and possibly add Teams later. We also discussed the possibility of creating extensions for Visual Studio Code and IntelliJ. Vault Versioning and Environment Profiles were considered but deemed not feasible due to similar constraints as the Teams feature.

Integration with Other Tools: This feature would involve providing an API that allows other tools to interact with your tool. We discussed the possibility of creating a REST API, a command-line interface, or a library that can be imported into other programs. We also discussed the need for security, as exposing an API could potentially make your tool more vulnerable to attacks.

Teams: We discussed the potential complexity and challenges of implementing a Teams feature, including the need for centralized control and coordination, and the potential for conflicts and inconsistencies. We decided to put this feature on hold for now.

IDE Extensions: We discussed the possibility of creating extensions for Visual Studio Code and IntelliJ. These extensions would use your tool's API to interact with the vault and provide a user-friendly interface for managing environment variables. We discussed the need for compatibility with a wide range of other tools and platforms, and the potential complexity of developing IDE extensions.

CLI Utility: We discussed the idea of creating a Command Line Interface (CLI) utility as a foundation for your IDE extensions. The CLI utility would allow users to interact with your tool directly from the command line, and could also be used by the IDE extensions to perform actions on the vault. We discussed the need for clear and helpful error messages, and the importance of testing the CLI utility to ensure it works correctly.

One-Time Sync: We discussed the possibility of a one-time sync feature, where a vault is sent over a wormhole and then becomes independent. We discussed the potential for out-of-sync variables between users, and the need for a strategy to handle this, such as an option for automatic updates.

Magic Wormhole: Magic Wormhole is a protocol for sending arbitrary-sized data from one computer to another. The sender generates a short, human-readable code that can be communicated over the phone or in person. The recipient enters this code into their own Magic Wormhole client, establishing a direct and secure connection between the two computers. We discussed using Magic Wormhole as a mechanism for sending the vault between users in a one-time sync scenario.

VS Code Extension Interaction with CLI: We discussed how a VS Code extension might interact with a CLI utility. We looked at an example of using Node.js's built-in child_process module to spawn a child process and run a command. We discussed the need for error handling and input validation in this context.

## Notes

- Minimize the cognitive load. 
- Tool should not store variable values in the vault, only keys. This is because I am only a transfer tool and not a storage tool. 
- Vault name validations - legal string keys for json? alphanuneric maybe? to avoid compatibility issues
- Allow users to bulk input a comma separated, space separated or new-line separated list of names of environment variables to a vault
- Tool should store variable names in a file inside a dot folder. Folder can live at $HOME level
- When sender sends a vault, tool should check whether env variable exists. If it doesn't exist, then ask user how to proceed. 
- When receiver receives a variable that already exists in their system, ask them how to proceed. Give them options like keep/overwrite/keep all/overwrite all. Give them option to view both the values before choosing. 
- Session variables are not in scope. Only system wide environment variables. But there's no good way to distinguish right now, so will keep it out of scope of MVP.
- Test between 2 macs, mac to ubuntu (and vice versa), ubuntu to ubuntu
- Guide the user through happy path using output from each command. 
- Running magicenv without any option should show them the help command. 
- Help command should give them a quickstart. Add vault and variables and press send. This will generate an OTP that should be entered by receiving system. 
- To export variables permanently, write to the user's shell startup script (bashrc, zshrc etc). Detect the shell using $SHELL command, then use the common startup scripts. If none of them are present, ask user whether it should be created for them.
- In the future, allow people to host their own relay and rendezvous servers.
- Add autocomplete to all commands
- Autocomplete should be dynamic - don't show existing items in the dropdown list
- What happens when receiver enters wrong code?
- What happens to export values when they are overwritten?

## Happy path flow

- User installs the tool using pip or brew
- They run the help function. This shows them that they should likely start with creating a new vault, then send the vault. Also ask receiver to install magicenv as well. 
- They run magicenv create vault1. This should prompt them to input environment variables (y/n question if they want to add now)
- They add env variables individually. After they press done, suggest in the output that they can run magicenv send vault1
- When they write the send command, validate that env variables that are being sent exist in the system, and then the code appears, similar to how it works for magic-wormhole
- Receiver receives the variable, tool checks if the variable is already present in the system, and because it doesnt exist, the variables are written into the system. 

## Potential pitfalls in the flow

- vault name validation
- sender's vault variables are not present in the system anymore
- receiver already has existing vault variables

## Interface

Create a new vault: magicenv create <vault_name>

This command creates a new vault with the given name.

Add environment variables to a vault: magicenv add <vault_name> <var1> <var2> ...

This command adds the specified environment variables to the vault. If a specified variable does not exist, the tool should prompt the user for how to proceed.

List all vaults: magicenv list

This command lists all existing vaults.

View a vault: magicenv view <vault_name>

This command displays the environment variables in the specified vault.

Send a vault to another user: magicenv send <vault_name>

This command sends the specified vault to another user via Magic Wormhole. The tool should generate a code for the recipient to enter.

Receive a vault from another user: magicenv receive <code>

This command receives a vault from another user. The user must enter the code provided by the sender. If a received variable already exists in the user's environment, the tool should prompt the user for how to proceed.

Delete a vault: magicenv delete <vault_name>

This command deletes the specified vault.

Help: magicenv --help

This command displays help information about how to use the tool.

## Suggested file structure

main.py: This is the entry point of your application. It should parse the command-line arguments and call the appropriate function based on the command entered by the user.

vault.py: This file should contain a Vault class that represents a vault. The class should have methods for each of the operations that can be performed on a vault, such as adding variables, deleting variables, and sending the vault to another user.

vault_manager.py: This file should contain a VaultManager class that manages all of the vaults. It should have methods for creating a new vault, deleting a vault, listing all vaults, and finding a vault by name.

cli.py: This file should contain functions for interacting with the user, such as prompting the user for input and displaying messages.

utils.py: This file should contain utility functions that are used in multiple places in your code, such as a function for validating environment variable names.

config.py: This file should contain configuration settings for your application, such as the path to the directory where the vaults are stored.

Here's how these files might interact:

When the user runs your application, main.py is executed. It parses the command-line arguments and calls a function in cli.py based on the command entered by the user.
The functions in cli.py interact with the user and call methods on the Vault and VaultManager classes to perform the requested operations.
The Vault and VaultManager classes use the utility functions in utils.py as needed.
The Vault and VaultManager classes read from and write to the vaults directory specified in config.py.
This structure separates concerns and makes your code easier to understand and maintain. It also makes it easier to test your code, as you can test each file independently.

## Points to cover in Readme.md

- Intro
- Quickstart
- Security
- Roadmap

## Build, publish and maintain

Write the Code: Develop your Python CLI tool. Include a shebang (#!/usr/bin/env python3) at the top of your script.

Write Tests: Write unit tests for your CLI tool using a framework like unittest or pytest.

Package Your Tool: Create a setup.py file for your project. This file includes information about your project and its dependencies. Also, create a __main__.py file that calls your main function when the package is run as a script.

Test Your Package: Test your package locally to ensure it works correctly. This includes running your unit tests and manually testing the tool.

Publish to PyPI: Publish your package to the Python Package Index (PyPI) so it can be installed with pip.

Create a Homebrew Formula: Write a Homebrew formula for your tool. This is a Ruby script that describes how to install your tool using pip.

Test Your Formula: Test your formula locally using brew install --build-from-source /path/to/your/formula.rb.

Create a Homebrew Tap: Create a Homebrew tap for your tool. This is a GitHub repository that contains Homebrew formulae.

Add Your Formula to the Tap: Add your formula to the tap by committing it to the tap's Git repository.

Set Up Continuous Integration: Set up a CI tool like Jenkins, Travis CI, or GitHub Actions. Configure it to run your tests, package your tool, and deploy it to PyPI and your Homebrew tap whenever you push changes to your repository.

Document Your Tool: Write clear documentation that explains how to install and use your tool. Include instructions for both pip and Homebrew installations.

Maintain Your Tool: After publishing, regularly update your tool with bug fixes, new features, and compatibility updates. Each time you update your tool, increment its version number and update its PyPI and Homebrew packages.

Versioning: Use semantic versioning for your tool. This helps users and contributors understand the scope of changes between releases.

Release Notes: For each new version, write release notes that describe the changes. This helps users understand what's new and whether they should upgrade.

Distribution Channels: In addition to PyPI and Homebrew, consider other distribution channels. For example, if your tool is useful for developers, you might want to publish it on developer-focused package managers like npm or RubyGems.

Licensing: Choose an appropriate license for your tool and include a LICENSE file in your repository. This tells users what they can and can't do with your software.

Contributing Guidelines: If you want to accept contributions from others, write clear contributing guidelines and include them in a CONTRIBUTING file in your repository.

Code of Conduct: To foster a healthy and respectful community around your project, consider adding a code of conduct.

Support: Decide how you'll provide support for your tool. This could be via an issue tracker, a mailing list, a chat room, or any other method you choose. Make sure to communicate this to your users.

Promotion: Promote your tool to reach potential users. This could involve presenting at meetups or conferences, writing blog posts, posting on social media, or any other method you choose.