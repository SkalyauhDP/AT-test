from pydantic import BaseModel
from typing import List, Literal


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class PetModel(BaseModel):
    id: int
    category: Category
    name: str
    photoUrls: List[str]
    tags: List[Tag]
    status: Literal["available", "pending", "sold"]
