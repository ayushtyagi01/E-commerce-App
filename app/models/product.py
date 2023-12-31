from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
    available_quantity: int

    class Config:
        orm_mode = True
