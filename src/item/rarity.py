from enum import Enum


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4


rarityRanges = {
    Rarity.COMMON: (1, 10),
    Rarity.UNCOMMON: (10, 30),
    Rarity.RARE: (30, 50),
    Rarity.EPIC: (50, 80),
    Rarity.LEGENDARY: (80, 100)
}


def rarity_from_number(rarity_number: int) -> Rarity:
    for rarity, (bottom, top) in rarityRanges.items():
        if bottom <= rarity_number <= top:
            return rarity
