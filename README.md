## What is this?

A CLI tool to share select environment variables with someone else, easily and securely. This is useful, for example, when you have a new person on your team and they need secrets and other configuration present in environment variables to run your company's software locally. 

This tool is built on top of [magic-wormhole](https://github.com/magic-wormhole/magic-wormhole), which allows for secure P2P transfer of data. In case a direct connection cannot be made (due to NAT gateways in the middle, for example), the data goes through an untrusted relay server. For known vulnerabilities of magic-wormhole, click [here](https://magic-wormhole.readthedocs.io/en/latest/attacks.html). 

When you will choose to send a collection of variables to someone, you will be given a one time code. Share that code with the receiver (through Slack, Teams, orally, whatever). Receiver will enter that code in their shell, and that's it. They will now have all the variables that you have shared with them. 

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