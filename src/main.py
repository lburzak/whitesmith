import os

from readchar import readkey

from inventory import Inventory
from inventory_view import InventoryView
from market import Market
from mining import Mine
from metal import Metal
from player import Player
from recipe import Recipe
from resources import generate_resources

from util import random_element
from views_root import ViewsRoot

res = generate_resources()
mine = Mine(res)
inv = Inventory()
market = Market()
player = Player(30, inv, 0)

ViewsRoot(
    player=player,
    mine=mine,
    resources=res,
    market=market
).start()

# LV = 70
# recipe = Recipe("test", 20, 2)
# metal = Metal("test", 20, 20)
#
# res = generate_resources()
#
# mine = Mine(res)
# inv = Inventory()
#
# for i in range(0, 100):
#     mine.mine(inv)
#
# iv: InventoryView
#
#
# def chg():
#     os.system("clear")
#     print(iv.render())
#
#
# iv = InventoryView(chg, inv)
# chg()
#
# c = '0'
#
# while c != 'q':
#     c = readkey()
#     iv.on_key(c)

# metals = [
#     generate_metal(Rarity.COMMON, 1),
#     generate_metal(Rarity.UNCOMMON, 1),
#     generate_metal(Rarity.RARE, 1),
#     generate_metal(Rarity.LEGENDARY, 1)
# ]
#
# buffer = {}
#
# for i in range(0, 100):
#     for mt in metals:
#         if randint(0, 1000) % mt.rarity == 0:
#             if buffer.get(mt.rarity):
#                 buffer[mt.rarity] += 1
#             else:
#                 buffer[mt.rarity] = 1
#
# if len(buffer) > 0:
#     print(buffer)
