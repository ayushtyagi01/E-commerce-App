from pydantic import BaseModel
from typing import List, Dict, Union
from datetime import datetime

class UserAddress(BaseModel):
    City: str
    Country: str
    ZipCode: str

class OrderItem(BaseModel):
    productName: str
    boughtQuantity: int
    TotalAmount: float

class OrderCreate(BaseModel):
    Items: List[Dict[str, Union[str, int, float]]]
    UserAddress: UserAddress

    def __str__(self):
        # Create a dictionary representation of the model
        order_dict = self.dict()
        # Convert the UserAddress field to a dictionary
        user_address_dict = self.UserAddress.dict()
        # Add the UserAddress dictionary to the main dictionary
        order_dict['UserAddress'] = user_address_dict
        # Use str() to get a string representation of the dictionary
        return str(order_dict)

class OrderInDB(OrderCreate):
    Timestamp: datetime

class Order(OrderInDB):
    id: str

class OrderInResponse(Order):
    class Config:
        orm_mode = True
