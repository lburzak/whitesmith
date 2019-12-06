from dataclasses import dataclass
from typing import Any, Dict, Optional
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

    def findRecordByItem(self, item: Any) -> Optional[InventoryRecord]:
        for record in self._records.values():
            if record.item == item:
                return record
        return None

    def take_item(self, item: Any, amount: int = 1) -> InventoryRecord:
        record = self.findRecordByItem(item)

        if record:
            if record.count >= amount:
                record.count -= amount
                return InventoryRecord(record.item, amount)

        return InventoryRecord(record.item, 0)

    def print_metals(self):
        for metal, count in [(record.item, record.count) for record in self._records.values() if isinstance(record.item, Metal)]:
            print("%s (%d) x%d" % (metal.name, metal.rarity, count))
