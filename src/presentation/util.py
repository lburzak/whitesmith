from inventory import InventoryRecord
from item_display import item_to_string


def inventory_record_to_list_row(record: InventoryRecord, type_tag: bool = False, verbose: bool = False) -> str:
    return "{:>3}x {}".format(record.count, item_to_string(record.item, type_tag=type_tag, verbose=verbose))
