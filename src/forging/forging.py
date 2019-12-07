from typing import Optional

import lang
from chance import calculate_forging_success_chance
from metal import Metal
from player import Player
from product import Product
from rarity import rarity_from_number, Rarity
from recipe import Recipe
from random import randint

from resources import Resources

RATING_MULTIPLIER_METAL = 3.2
RATING_MULTIPLIER_DIFFICULTY = 2
RATING_MULTIPLIER_SIZE = 0.2
SCRAP = Product(name="Odłamek", rating=0, rarity=Rarity.TRASH)


def randomize_rate(r: int):
    fluctuation = r // 5
    randomized = randint(r - fluctuation, r + fluctuation)
    if randomized < 0:
        randomized = 0 + randomized // 2
    return randomized


def rate(effective_difficulty: int, metal_rarity: int, size: int) -> int:
    size_rating = size * RATING_MULTIPLIER_SIZE
    difficulty_rating = effective_difficulty * RATING_MULTIPLIER_DIFFICULTY
    metal_rating = metal_rarity * RATING_MULTIPLIER_METAL * RATING_MULTIPLIER_METAL
    return round(size_rating * (difficulty_rating + metal_rating) // 10)


def forge(level: int, recipe: Recipe, metal: Metal) -> Product:
    effective_difficulty = get_effective_difficulty(metal, recipe)
    chance = calculate_forging_success_chance(level, effective_difficulty)
    rand = randint(1, 100)
    if rand > 100 - (chance * 100):
        actual_rate = rate(effective_difficulty, metal.rarity, recipe.size)
        name = lang.noun_to_adj(metal.name, recipe.product_name).capitalize() + " " + recipe.product_name.capitalize()
        return Product(name=name, rating=actual_rate, rarity=rarity_from_number(metal.rarity))
    else:
        return SCRAP


def get_effective_difficulty(metal: Metal, recipe: Recipe):
    return recipe.difficulty + metal.difficulty


def produce(player: Player, resources: Resources, recipe: Recipe, metal: Metal) -> Optional[Product]:
    inv_record = player.inventory.take_item(metal, recipe.size)
    product = None
    if inv_record.count >= recipe.size:
        product = forge(player.get_forging_level(), recipe, metal)
        res_record = resources.findByData(product)
        if res_record is None:
            res_record = resources.register(product)
        player.inventory.store_item(res_record, 1)
    return product
