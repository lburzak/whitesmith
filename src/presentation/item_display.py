from typing import Any

import colorama

from metal import Metal
from product import Product
from rarity import Rarity, rarity_from_number
from recipe import Recipe


def with_formatting(string: str, rarity: Rarity) -> str:
    formatting = colorama.Style.BRIGHT
    if rarity is Rarity.UNCOMMON:
        formatting += colorama.Fore.GREEN
    elif rarity is Rarity.RARE:
        formatting += colorama.Fore.BLUE
    elif rarity is Rarity.EPIC:
        formatting += colorama.Fore.MAGENTA
    elif rarity is Rarity.LEGENDARY:
        formatting += colorama.Fore.RED
    return formatting + string + colorama.Style.RESET_ALL


def get_item_core(item: Any) -> str:
    if isinstance(item, Metal):
        return item.name
    elif isinstance(item, Recipe):
        return item.product_name.capitalize()
    elif isinstance(item, Product):
        return item.name
    else:
        raise Exception("Not an item")


def get_type_tag(item: Any) -> str:
    if isinstance(item, Metal):
        return "[Metal]"
    elif isinstance(item, Recipe):
        return "[Przepis]"
    elif isinstance(item, Product):
        return "[Produkt]"
    else:
        raise Exception("Not an item")


def get_additional_info(item: Any) -> str:
    if isinstance(item, Product):
        return "(%d)" % item.rating
    else:
        return ""


def get_item_rarity(item: Any) -> Rarity:
    if isinstance(item, Metal):
        return rarity_from_number(item.rarity)
    elif isinstance(item, Recipe):
        return Rarity.COMMON
    elif isinstance(item, Product):
        return Rarity.COMMON
    else:
        raise Exception("Not an item")


def item_to_string(item: Any, embedded: bool = False, type_tag: bool = False, verbose: bool = False) -> str:
    core = get_item_core(item)
    tag = get_type_tag(item) + " " if type_tag else ""
    additional_info = get_additional_info(item) if verbose else ""
    compound = tag + core + additional_info
    enclosed = "[%s]" % compound if embedded else compound
    formatted = with_formatting(enclosed, get_item_rarity(item))
    return formatted

