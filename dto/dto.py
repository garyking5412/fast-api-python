from typing import List

from pydantic import BaseModel

class ProductRequest(BaseModel):
    name: str
    detail: str
    image: str
    price: int

class CategoryRequest(BaseModel):
    name: str
    detail: str
    products: List[ProductRequest]

class ProductResponse(BaseModel):
    id: int
    name: str
    detail: str
    image: str
    price: int

class CategoryResponse(BaseModel):
    id: int
    name: str
    detail: str
    products: List[ProductResponse]