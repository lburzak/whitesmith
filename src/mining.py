from functools import reduce
from typing import List

from inventory import Inventory
from metal import Metal
from player import Player
from resources import Resources, ResourceRecord
from random import randint


class Mine:
    res: Resources
    metals: List[ResourceRecord]

    def __init__(self, res: Resources):
        self.res = res
        self.metals = res.get_metals()

    def get_effective_rarity(self, player: Player, rarity: int):
        effective_rarity = rarity - player.mining_gauge.level
        if effective_rarity >= 1:
            return effective_rarity
        else:
            return 1

    def mine(self, player: Player) -> [Metal]:
        obtained_metals = []
        for metal in self.metals:
            if randint(0, self.get_effective_rarity(player, metal.data.rarity)) == 0:
                obtained_metals.append(metal)
                player.inventory.store_item(metal, 1)
        player.on_mining(sum([metal.data.rarity for metal in obtained_metals]))
        return obtained_metals
