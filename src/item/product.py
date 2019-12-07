from dataclasses import dataclass

from rarity import Rarity


@dataclass
class Product:
    name: str
    rating: int
    rarity: Rarity
