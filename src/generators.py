from lang import generate_metal_name
from random import randint

from metal import Metal
from rarity import Rarity, rarityRanges


def random_rarity(rarity: Rarity):
    bottom, top = rarityRanges[rarity]
    return randint(bottom, top)


def generate_metal(rarity: Rarity, level_ten: int) -> Metal:
    name = generate_metal_name()
    rarity = random_rarity(rarity)
    min_difficulty = level_ten * 10
    max_difficulty = min_difficulty + 10
    difficulty = randint(min_difficulty, max_difficulty)
    return Metal(name, difficulty, rarity)
