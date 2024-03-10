from medication import Medication
from storage import Storage


class MedicationManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.medications = []

    def load_medications(self):
        self.medications = self.storage.load_medications() or []

    def add_medication(self, name, box_quantity, box_count, daily_dose, remaining_doses, consumption_times):
        medication = Medication(name, box_quantity, box_count, daily_dose, remaining_doses, consumption_times)
        self.medications.append(medication)
        self.storage.save_medications(self.medications)

    def confirm_intake(self, medication_name):
        for medication in self.medications:
            if medication.name == medication_name:
                medication.remaining_doses -= 1
                self.storage.save_medications(self.medications)
                return
        raise ValueError(f"Medication '{medication_name}' does not exist")