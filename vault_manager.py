import json
import os
from vault import Vault
from config import VAULTS_STORAGE

class VaultManager:
    def __init__(self):
        self.vaults = self.load_vaults()

    def load_vault(self, name, throw_error=True):
        if name in self.vaults:
            return self.vaults[name]
        else:
            if throw_error:
                raise ValueError(f"Vault '{name}' does not exist.")
            else:
                return None

    def load_vaults(self):
        if os.path.exists(VAULTS_STORAGE):
            with open(VAULTS_STORAGE, 'r') as f:
                data = json.load(f)
                return {name: Vault(name) for name in data}
        else:
            return {}

    def save_vaults(self):
        vaults_data = {name: list(vault.variables) for name, vault in self.vaults.items()}
        with open(VAULTS_STORAGE, 'w') as f:
            json.dump(vaults_data, f)
        for vault in self.vaults.values():
            vault.save_variables()
    
    def create_vault(self, name):
        if name not in self.vaults:
            self.vaults[name] = Vault(name)
            self.save_vaults()

    def delete_vault(self, name):
        if name in self.vaults:
            del self.vaults[name]
            self.save_vaults()

    def list_vaults(self):
        return list(self.vaults.keys())