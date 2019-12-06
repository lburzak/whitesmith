from typing import Callable

from readchar import key

from inventory import Inventory
from mining import Mine
from view import View, KeyListener


class MineView(View, KeyListener):
    last_mining_result = []
    mine: Mine
    inventory: Inventory
    on_change: Callable

    def __init__(self, on_change: Callable, mine: Mine, inventory: Inventory):
        self.mine = mine
        self.inventory = inventory
        self.on_change = on_change

    def on_key(self, k: key):
        if k == key.SPACE:
            self.last_mining_result = self.mine.mine(self.inventory)
            self.on_change()

    def render(self) -> str:
        names = [record.data.name for record in self.last_mining_result]
        if len(names) == 0:
            return "Nic nie wykopałeś!"
        else:
            return "Wykopałeś: \n\t" + "\n\t".join(names)
