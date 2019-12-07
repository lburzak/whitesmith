from typing import Callable

from readchar import key

from presentation.item_display import item_to_string
from presentation.list_view import ListView
from presentation.view import View, KeyListener
from inventory import InventoryRecord
from market import Market
from player import Player


class MarketView(View, KeyListener):
    sellable_goods_list_view = ListView([])
    market: Market
    player: Player
    on_change: Callable

    def __init__(self, on_change: Callable, player: Player, market: Market):
        self.market = market
        self.player = player
        self.on_change = on_change

    def render(self) -> str:
        items = ["%dx %s" % (record.count, item_to_string(record.item, verbose=True)) for record in self.player.inventory.find_products()]
        self.sellable_goods_list_view.items = items
        return self.render_balance() + "\n\n" + self.sellable_goods_list_view.render()

    def on_key(self, k: key):
        if k == key.UP:
            self.sellable_goods_list_view.up()
        elif k == key.DOWN:
            self.sellable_goods_list_view.down()
        elif k == key.ENTER:
            self.attempt_selling()
        self.on_change()

    def render_balance(self) -> str:
        return "Złoto: %d" % self.player.money

    def attempt_selling(self):
        if len(self.sellable_goods_list_view.items) > 0:
            withdrawal_record = self.player.inventory.take_item(self.get_selected_record().item, 1)
            self.market.sell_item(self.player, withdrawal_record)

    def get_selected_record(self) -> InventoryRecord:
        products = self.player.inventory.find_products()
        return products[self.sellable_goods_list_view.pos]

    def handle_up(self):
        pass

    def handle_down(self):
        pass
