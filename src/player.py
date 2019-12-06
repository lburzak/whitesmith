from dataclasses import dataclass
from inventory import Inventory


@dataclass
class Player:
    forging_level: int
    inventory: Inventory
