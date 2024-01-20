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

- Tool should not store variable values in the vault, only keys. This is because I am only a transfer tool and not a storage tool. 
- Tool should store variable names in a file inside a dot folder. Folder can live at $HOME level
- When sender sends a vault, tool should check whether env variable exists. If it doesn't exist, then ask user how to proceed. 
- When receiver receives a variable that already exists in their system, ask them how to proceed. Give them options like keep/overwrite/keep all/overwrite all. 
- Session variables are not in scope. Only system wide environment variables. But there's no good way to distinguish right now, so will keep it out of scope of MVP.

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