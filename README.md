## What is this?

A CLI tool to share select environment variables with someone else, easily and securely. 

This tool is built on top of [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole), which allows for secure, accountless P2P transfer of data. 

When you use `sendenv` to send a collection (called `vault`) of variables to someone, a one time code will be generated and shown to you. Share that code with the receiver (through Slack, Teams, orally, whatever). Receiver will enter that code in their shell and have all the variables loaded into their environment. 

### Example use cases

1. A new member has joined your team and needs to set up a ton of environment variables to run your company's code locally. You can use `sendenv` to set up a vault of all your necessary variables once, and share with as many people, as many times as you need to.
2. If you run your code on a separate environment in addition to your local environment, and want to get all your environment variables from your local to the separate environment, you can use `sendenv` to replicate environment variable on the separate environment easily. 

## How do I use this?

Install `sendenv` for both the sender and receiver. 

```bash
pip install sendenv
```

To send environment variables

```bash
# create vault (a collection of variables that you want to send)
sendenv create-vault your_vault_name

## Add environment variables that you want to share to the vault. 
sendenv add-var your_vault_name
## You will be prompted to add variable names.

## Send the vault to someone
sendenv send-vault your_vault_name
## You will see something like the following:
## Code: 1-aardvark-pillow
## Give this code to the receiver.
```

At receiver's end

```bash

sendenv receive-vault
## This will prompt you for the code you received from the sender. Enter it here. 
## Now the variables are loaded into your system (exported in your shell RC file).
```

### Other commands

Access all commands and understand their use by typing `sendenv -h` or just `sendenv`. 