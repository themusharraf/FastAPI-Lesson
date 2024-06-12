from typing import List, Optional
from pydantic import BaseModel, Field
from enum import Enum


class Types(Enum):
    customer = "customer"
    expert = "expert"


class Type(BaseModel):
    id: int
    create_at: str
    type: Types


class Books(BaseModel):
    id: int
    user_id: int
    title: str = Field(min_length=10)
    price: float = Field(ge=0)


class Users(BaseModel):
    id: int
    role: str
    name: str
    type: Optional[List[Type]]


users_db = [
    {"id": 1, "role": "admin", "name": "Musharraf"},
    {"id": 2, "role": "investor", "name": "Musharraf"},
    {"id": 3, "role": "customer", "name": "Musharraf", "type": [
        {"id": 1, "create_at": "2024-01T00:00:00", "type": "expert"}
    ]},

]

book_db = [
    {"id": 1, "userid": 2, "title": "Deep Work", "price": 24.000},
    {"id": 2, "userid": 1, "title": "Rich Father", "price": 25.000},
    {"id": 3, "userid": 2, "title": "Data Since book", "price": 23.000},
    {"id": 4, "userid": 4, "title": "Python cookbook", "price": 20.000}
]
