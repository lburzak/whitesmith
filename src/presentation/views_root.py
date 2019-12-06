import os
from typing import Union, Dict

from readchar import readkey, key

from forge_view import ForgeView
from inventory import Inventory
from inventory_view import InventoryView
from market import Market
from market_view import MarketView
from menu_view import MenuView
from mine_view import MineView
from mining import Mine
from player import Player
from resources import Resources
from view import View, KeyListener


class ViewsRoot:
    current_view: View
    controls_listener: KeyListener
    routes: Dict[str, View]

    def __init__(self, player: Player, mine: Mine, resources: Resources, market: Market):
        self.routes = {
            "Magazyn": InventoryView(self.change_handler, player.inventory),
            "Kopalnia": MineView(self.change_handler, mine, player.inventory),
            "Kuźnia": ForgeView(self.change_handler, player, resources),
            "Bazar": MarketView(self.change_handler, player, market)
        }

        self.routes["Menu"] = MenuView(self.change_handler, self.open_route, list(self.routes.keys()))

        self.open_route("Menu")

    def set_view(self, new_view: Union[View, KeyListener]):
        self.current_view = new_view
        self.controls_listener = new_view

    def change_handler(self):
        os.system("clear")
        print(self.current_view.render())

    def open_route(self, route_name: str):
        self.set_view(self.routes[route_name])
        self.change_handler()

    def start(self):
        self.change_handler()
        while True:
            c = readkey()
            if c == 'q':
                break
            elif c == key.BACKSPACE or c == key.ESC:
                self.open_route("Menu")
            else:
                self.controls_listener.on_key(c)
