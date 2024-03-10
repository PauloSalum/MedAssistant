from dataclasses import dataclass


@dataclass
class Medication:
    name: str
    box_quantity: int
    box_count: int
    daily_dose: int
    remaining_doses: int
    consumption_times: list
