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
    _current_view: View
    _controls_listener: KeyListener
    _routes: Dict[str, View]

    def set_routes(self, routes: Dict[str, View]):
        self._routes = routes

    def set_view(self, new_view: Union[View, KeyListener]):
        self._current_view = new_view
        self._controls_listener = new_view

    def change_handler(self):
        os.system("clear")
        print(self._current_view.render())

    def open_route(self, route_name: str):
        view = self._routes.get(route_name)
        if view:
            self.set_view(view)
            self.change_handler()
        else:
            raise Exception("No such route: %s" % route_name)

    def start(self, initial_route_name: str):
        if not self._routes:
            raise Exception("Routes not set.")
        self.open_route(initial_route_name)
        self.change_handler()
        while True:
            c = readkey()
            if c == 'q':
                break
            elif c == key.BACKSPACE or c == key.ESC:
                self.open_route("Menu")
            else:
                self._controls_listener.on_key(c)
