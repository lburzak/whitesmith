from dataclasses import dataclass
from operator import attrgetter
from typing import Any, Dict, Optional

from items import Metal, Product
from resources import ResourceRecord


@dataclass
class InventoryRecord:
    item: Any
    count: int


class Inventory:
    _records: Dict[int, InventoryRecord] = {}

    def store_item(self, res: ResourceRecord, count: int):
        if res.id in self._records:
            self._records[res.id].count += count
        else:
            self._records[res.id] = InventoryRecord(res.data, count)

    def get_records(self) -> Dict[int, InventoryRecord]:
        return self._records

    def find_record_by_item(self, item: Any) -> Optional[InventoryRecord]:
        for record in self._records.values():
            if record.item == item:
                return record
        return None

    def remove_record(self, record: InventoryRecord):
        for key in self._records.keys():
            if self._records[key] == record:
                del self._records[key]
                break

    def take_item(self, item: Any, amount: int = 1) -> InventoryRecord:
        record = self.find_record_by_item(item)

        if record:
            if record.count >= amount:
                record.count -= amount
                if record.count == 0:
                    self.remove_record(record)
                return InventoryRecord(record.item, amount)

        return InventoryRecord(None, 0)

    def find_metals(self, sort=False) -> [InventoryRecord]:
        metals = [record for record in self._records.values() if isinstance(record.item, Metal)]
        if sort:
            return sorted(metals, key=attrgetter("count"), reverse=True)
        else:
            return metals

    def find_products(self, sort=False) -> [InventoryRecord]:
        products = [record for record in self._records.values() if isinstance(record.item, Product)]
        if sort:
            return sorted(products, key=attrgetter("count"), reverse=True)
        else:
            return products
