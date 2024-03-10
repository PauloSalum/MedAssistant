from medication_entity import MedicationEntity
from medication_manager import MedicationManager
from storage import Storage


class MedAssistant:
    def __init__(self, hass, config):
        self.hass = hass
        # Ler a entidade de notificação da configuração
        self.notify_entity = config.get('notify_entity', 'notify.notify')
        self.storage = Storage()
        self.medication_manager = MedicationManager(self.storage)

    def setup(self):
        self.medication_manager.load_medications()
        self.register_services()
        self.update_entities()
        return True

    def update_entities(self):
        entities = [MedicationEntity(med) for med in self.medication_manager.medications]
        self.hass.add_job(self.hass.helpers.entity_component.async_add_entities(entities))

    def register_services(self):
        self.hass.services.async_register("medassistant", "add_medication", self.add_medication_service)
        self.hass.services.async_register("medassistant", "confirm_intake", self.confirm_intake_service)

    async def add_medication_service(self, call):
        name = call.data.get("name")
        box_quantity = call.data.get("box_quantity")
        box_count = call.data.get("box_count")
        daily_dose = call.data.get("daily_dose")
        remaining_doses = call.data.get("remaining_doses")
        consumption_times = call.data.get("consumption_times")

        self.medication_manager.add_medication(name, box_quantity, box_count, daily_dose, remaining_doses,
                                               consumption_times)
        self.update_entities()

    async def confirm_intake_service(self, call):
        medication_name = call.data.get("medication_name")
        try:
            self.medication_manager.confirm_intake(medication_name)
            self.update_entities()
            # Corrigido para passar 'notify_entity' adequadamente
            self.notification_manager.send_consumption_notification(medication_name, self.hass)
        except ValueError as e:
            self.hass.components.persistent_notification.create(
                f"Error: {str(e)}",
                title="MedAssistant Error",
                notification_id="medassistant_error"
            )


def setup(hass, config):
    med_assistant = MedAssistant(hass, config['medassistant'])
    return med_assistant.setup()
