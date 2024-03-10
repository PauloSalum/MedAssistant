from homeassistant.helpers.entity import Entity


class MedicationEntity(Entity):
    def __init__(self, medication):
        self._medication = medication
        self.entity_id = f"medassistant.{medication.name.replace(' ', '_').lower()}"
        self._state = "pending"

    @property
    def name(self):
        return self._medication.name

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return {
            "box_quantity": self._medication.box_quantity,
            "box_count": self._medication.box_count,
            "daily_dose": self._medication.daily_dose,
            "remaining_doses": self._medication.remaining_doses,
            "consumption_times": self._medication.consumption_times,
        }
