from inventory import InventoryRecord
from player import Player
from product import Product


class Market:
    def calculate_price(self, rating: int) -> int:
        return rating

    def sell_item(self, player: Player, withdrawal_record: InventoryRecord) -> int:
        if isinstance(withdrawal_record.item, Product):
            price = self.calculate_price(withdrawal_record.item.rating)
            player.pay(price)
            return price
        else:
            raise Exception("Selling goods other than `Product` not implemented", withdrawal_record.item)
