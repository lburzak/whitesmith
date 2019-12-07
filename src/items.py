from dataclasses import dataclass
from enum import Enum


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EPIC = 3
    LEGENDARY = 4
    TRASH = 5


@dataclass
class Metal:
    name: str
    difficulty: int
    rarity: int


@dataclass
class Product:
    name: str
    rating: int
    rarity: Rarity


@dataclass
class Recipe:
    product_name: str
    difficulty: int
    size: int

rarityRanges = {
    Rarity.TRASH: (0, 0),
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