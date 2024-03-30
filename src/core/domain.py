from typing import Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Owner:
    id: int
    name: str
    email: str
    phone_number: Optional[str]
    created_at: Optional[datetime]

@dataclass
class Pet:
    id: int
    name: str
    species: str
    breed: Optional[str]
    age: Optional[int]
    owner_id: Optional[int]
    created_at: Optional[datetime]
