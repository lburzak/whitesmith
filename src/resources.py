from dataclasses import dataclass
from typing import Dict, Any, Optional

from generators import generate_metal
from items import Metal, Rarity


@dataclass
class ResourceRecord:
    id: int
    data: Any


class Resources:
    _lastIndex: int = -1
    _data: Dict[int, Any] = {}

    def register(self, resource: Any) -> ResourceRecord:
        index = self._lastIndex + 1
        self._data[index] = resource
        self._lastIndex = index
        return ResourceRecord(index, resource)

    def findById(self, rid: int) -> Optional[Any]:
        return self._data[rid]

    def findByData(self, data: Any) -> Optional[ResourceRecord]:
        for key, res_data in self._data.items():
            if res_data == data:
                return ResourceRecord(key, res_data)
        return None

    def get_metals(self):
        return [ResourceRecord(key, data) for key, data in self._data.items() if isinstance(data, Metal)]


generator_conf = {
    "metals": {
        Rarity.COMMON: 2,
        Rarity.UNCOMMON: 3,
        Rarity.RARE: 3,
        Rarity.EPIC: 3,
        Rarity.LEGENDARY: 2
    }
}


def generate_resources() -> Resources:
    res = Resources()
    for rarity, count in generator_conf["metals"].items():
        for i in range(0, count):
            res.register(generate_metal(rarity, 1))
    return res
