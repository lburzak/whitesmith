from dataclasses import dataclass


@dataclass
class Recipe:
    product_name: str
    difficulty: int
    size: int
