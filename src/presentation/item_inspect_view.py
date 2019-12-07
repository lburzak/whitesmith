from presentation.item_display import item_to_string
from items import Metal, Product, Recipe


class ItemInspectView:
    def render(self, item) -> str:
        if isinstance(item, Metal):
            return "%s:\n\tTrudność: %d\n\tRzadkość: %d" % (item_to_string(item, type_tag=True), item.difficulty, item.rarity)
        elif isinstance(item, Product):
            return "%s:\n\tOcena: %d" % (item_to_string(item, type_tag=True), item.rating)
        elif isinstance(item, Recipe):
            return "%s:\n\tTrudność: %d\n\tGabaryty: %d" % (item_to_string(item, type_tag=True), item.difficulty, item.size)
        elif item is None:
            return ""
        else:
            raise Exception("Unknown item: ", item)
