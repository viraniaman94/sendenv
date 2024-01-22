import os

# Define the path to the directory where the vaults are stored
VAULTS_DIR = os.path.expanduser("~/.magicenv")

# Define the path to the vaults configuration file
VAULTS_CONFIG = os.path.join(VAULTS_DIR, "config.json")

# Define the path to the vault storage file
VAULTS_STORAGE = os.path.join(VAULTS_DIR, "storage.json")

WORMHOLE_APP_ID = "magicenv.dev"