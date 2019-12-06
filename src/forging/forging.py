import lang
from chance import calculate_forging_success_chance
from metal import Metal
from player import Player
from product import Product
from recipe import Recipe
from random import randint


RATING_MULTIPLIER_METAL = 20
RATING_MULTIPLIER_DIFFICULTY = 20
RATING_MULTIPLIER_SIZE = 4
SCRAP = Product(name="Scrap", rating=0)


def randomize_rate(r: int):
    fluctuation = r // 5
    randomized = randint(r - fluctuation, r + fluctuation)
    if randomized < 0:
        randomized = 0 + randomized // 2
    return randomized


def rate(effective_difficulty: int, metal_rarity: int, size: int):
    return effective_difficulty * RATING_MULTIPLIER_DIFFICULTY\
           + metal_rarity * RATING_MULTIPLIER_METAL\
           + size * RATING_MULTIPLIER_SIZE


def forge(level: int, recipe: Recipe, metal: Metal) -> Product:
    effective_difficulty = get_effective_difficulty(metal, recipe)
    chance = calculate_forging_success_chance(level, effective_difficulty)
    rand = randint(1, 100)
    if rand > 100 - (chance * 100):
        actual_rate = randomize_rate(rate(effective_difficulty, metal.rarity, recipe.size))
        name = lang.noun_to_adj(metal.name).capitalize() + " " + recipe.product_name.capitalize()
        return Product(name=name, rating=actual_rate)
    else:
        return Product(name="Scrap", rating=0)


def get_effective_difficulty(metal: Metal, recipe: Recipe):
    return recipe.difficulty + metal.difficulty


def produce(player: Player, recipe: Recipe, metal: Metal):
    if player.inventory.
