from dataclasses import dataclass
from typing import Optional

# Definieren der Eigenschaften eines Buches

@dataclass
class Book:
    id: Optional[int]
    title: str
    author: str
    year: Optional[int] = None  