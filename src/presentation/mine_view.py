from typing import Callable

from readchar import key

from mining import Mine
from player import Player
from presentation.view import View, KeyListener
from presentation.item_display import item_to_string


class MineView(View, KeyListener):
    last_mining_result = []
    mine: Mine
    player: Player
    on_change: Callable

    def __init__(self, on_change: Callable, mine: Mine, player: Player):
        self.mine = mine
        self.player = player
        self.on_change = on_change

    def on_key(self, k: key):
        if k == key.SPACE:
            self.last_mining_result = self.mine.mine(self.player)
            self.on_change()

    def render(self) -> str:
        items = [item_to_string(record.data, embedded=True) for record in self.last_mining_result]
        if len(items) == 0:
            return "Nic nie wykopałeś!"
        else:
            return "Wykopałeś: \n\t" + "\n\t".join(items)
