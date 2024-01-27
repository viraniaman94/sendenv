import json
import os
from config import VAULTS_STORAGE

class Vault:
    def __init__(self, name):
        self.name = name
        self.variables = self.load_variables()

    def load_variables(self):
        if os.path.exists(VAULTS_STORAGE):
            with open(VAULTS_STORAGE, 'r') as f:
                data = json.load(f)
                return data.get(self.name, [])
        else:
            return []

    def save_variables(self):
        if os.path.exists(VAULTS_STORAGE):
            with open(VAULTS_STORAGE, 'r') as f:
                data = json.load(f)
        else:
            data = {}
        data[self.name] = self.variables
        with open(VAULTS_STORAGE, 'w') as f:
            json.dump(data, f)

    def add_variable(self, variable):
        if variable not in self.variables:
            self.variables.append(variable)
            self.save_variables()

    def delete_variable(self, variable):
        if variable in self.variables:
            self.variables.remove(variable)
            self.save_variables()

    def list_variables(self):
        return self.variables