import unittest

import pytest

from medication_manager import MedicationManager
from storage import Storage


class TestMedAssistant(unittest.TestCase):
    def setUp(self):
        self.storage = Storage()
        self.medication_manager = MedicationManager(self.storage)

    def tearDown(self):
        self.storage.clear()

    def test_load_medications_with_empty_storage(self):
        self.medication_manager.load_medications()
        self.assertEqual(len(self.medication_manager.medications), 0)

    def test_add_medication_increases_count(self):
        storage = Storage()
        medication_manager = MedicationManager(storage)
        medication_manager.add_medication("TestMed", 10, 2, 1, 20, ["08:00", "20:00"])
        assert len(medication_manager.medications) == 1

    def test_add_medication_persists_to_storage(self):
        storage = Storage()
        medication_manager = MedicationManager(storage)
        medication_manager.add_medication("TestMed", 10, 2, 1, 20, ["08:00", "20:00"])
        assert len(storage.load_medications()) == 1

    def test_confirm_intake_reduces_remaining_doses(self):
        storage = Storage()
        medication_manager = MedicationManager(storage)
        medication_manager.add_medication("TestMed", 10, 2, 1, 20, ["08:00", "20:00"])
        medication_manager.confirm_intake("TestMed")
        assert medication_manager.medications[0].remaining_doses == 19

    def test_confirm_intake_persists_to_storage(self):
        storage = Storage()
        medication_manager = MedicationManager(storage)
        medication_manager.add_medication("TestMed", 10, 2, 1, 20, ["08:00", "20:00"])
        medication_manager.confirm_intake("TestMed")
        assert storage.load_medications()[0].remaining_doses == 19

    def test_confirm_intake_for_non_existent_medication(self):
        storage = Storage()
        medication_manager = MedicationManager(storage)
        medication_manager.add_medication("TestMed", 10, 2, 1, 20, ["08:00", "20:00"])
        with pytest.raises(ValueError):
            medication_manager.confirm_intake("NonExistentMed")


# Run the tests
if __name__ == "__main__":
    pytest.main()
