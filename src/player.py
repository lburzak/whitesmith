from inventory import Inventory
from leveling import ForgingGauge


class Player:
    forging_gauge: ForgingGauge = ForgingGauge(1, 0)
    inventory: Inventory
    money: int

    def __init__(self, inventory: Inventory, money: int):
        self.inventory = inventory
        self.money = money

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

    def get_forging_level(self) -> int:
        return self.forging_gauge.level

    def on_forging_successful(self, difficulty):
        self.forging_gauge.grant_xp(difficulty)

    def on_forging_failure(self, difficulty):
        self.forging_gauge.grant_xp(difficulty // 8)

