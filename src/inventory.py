from dataclasses import dataclass
from typing import Any, Dict
from metal import Metal
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

    def contains(self, resource_id: int, amount: int = 1) -> bool:
        record = self._records.get(resource_id)
        return record and record.count >= amount

    def take_item(self, resource_id: int, amount: int = 1):
        self

    def print_metals(self):
        for metal, count in [(record.item, record.count) for record in self._records.values() if isinstance(record.item, Metal)]:
            print("%s (%d) x%d" % (metal.name, metal.rarity, count))
