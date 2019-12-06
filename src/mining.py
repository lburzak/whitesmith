from typing import List

from inventory import Inventory
from metal import Metal
from resources import Resources, ResourceRecord
from random import randint


class Mine:
    res: Resources
    metals: List[ResourceRecord]

    def __init__(self, res: Resources):
        self.res = res
        self.metals = res.get_metals()

    def mine(self, inventory: Inventory) -> [Metal]:
        obtained_metals = []
        for mt in self.metals:
            if randint(0, 1000) % mt.data.rarity == 0:
                obtained_metals.append(mt)
                inventory.store_item(mt, 1)
        return obtained_metals

