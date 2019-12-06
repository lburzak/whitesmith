from dataclasses import dataclass
from inventory import Inventory


@dataclass
class Player:
    forging_level: int
    inventory: Inventory
    money: int

    def can_afford(self, amount: int) -> bool:
        return self.money >= amount

    def charge(self, amount: int) -> bool:
        if self.can_afford(amount):
            self.money -= amount
            return True
        else:
            return False

    def pay(self, amount: int):
        self.money += amount
