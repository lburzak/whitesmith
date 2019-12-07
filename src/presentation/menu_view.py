from dataclasses import dataclass
from typing import Callable

from readchar import key

from presentation.list_view import ListView
from presentation.view import View, KeyListener


@dataclass
class MenuRoute:
    title: str
    view: View


class MenuView(View, KeyListener):
    on_change: Callable
    on_route_selected: Callable
    menu_list_view: ListView
    routes: [str]

    def __init__(self, on_change: Callable, on_route_selected: Callable, routes: [str]):
        self.routes = routes
        self.on_change = on_change
        self.on_route_selected = on_route_selected
        self.menu_list_view = ListView(routes)

    def render(self) -> str:
        hint = "Naciśnij '?' aby pokazać/ukryć pomoc, 'q' aby wyjść.\n\n"
        return hint + self.menu_list_view.render()

    def on_key(self, k: key):
        if k == key.UP:
            self.menu_list_view.up()
        elif k == key.DOWN:
            self.menu_list_view.down()
        elif k == key.ENTER:
            route = self.routes[self.menu_list_view.pos]
            self.on_route_selected(route)
        self.on_change()
