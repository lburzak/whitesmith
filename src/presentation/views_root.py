import os
import sys
from typing import Union, Dict

from readchar import readkey, key

from presentation.controls_bar import ControlsBar
from presentation.top_bar_view import TopBarView
from presentation.view import View, KeyListener


class ViewsRoot:
    _current_view: View
    _current_route: str
    _controls_listener: KeyListener
    _routes: Dict[str, View]
    top_bar_view: TopBarView
    controls_bar = ControlsBar()
    show_controls = False
    clear_command = "cls" if sys.platform == "windows" else "clear"

    def set_routes(self, routes: Dict[str, View]):
        self._routes = routes

    def set_view(self, new_view: Union[View, KeyListener]):
        self._current_view = new_view
        self._controls_listener = new_view

    def clear_display(self):
        os.system(self.clear_command)

    def change_handler(self):
        self.clear_display()
        controls_render = ("\n" + self.controls_bar.render(self._current_route)) if self.show_controls else "\n"
        print(self.top_bar_view.render(self._current_route) + controls_render + "\n\n" + self._current_view.render())

    def open_route(self, route_name: str):
        view = self._routes.get(route_name)
        if view:
            self.set_view(view)
            self._current_route = route_name
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
            if c == '?':
                self.show_controls = not self.show_controls
                self.change_handler()
            elif c == key.BACKSPACE or c == key.ESC:
                self.open_route("Menu")
            else:
                self._controls_listener.on_key(c)
