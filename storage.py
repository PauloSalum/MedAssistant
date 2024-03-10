import json
from medication import Medication


class Storage:
    def __init__(self):
        self.file_path = "medications.json"

    def load_medications(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return [Medication(**med) for med in data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_medications(self, medications):
        with open(self.file_path, "w") as file:
            json.dump([med.__dict__ for med in medications], file)

    def clear(self):
        with open(self.file_path, "w") as file:
            file.write("")
