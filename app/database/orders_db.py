from typing import List
from .connection import db
from ..models.order import OrderCreate, OrderInDB
from bson import ObjectId
from datetime import datetime

def create_order(order: OrderCreate) -> OrderInDB:
    user_address = {
        "City": order.UserAddress.City,
        "Country": order.UserAddress.Country,
        "ZipCode": order.UserAddress.ZipCode,
    }
    
    new_order = {
        "Timestamp": datetime.now(),
        "Items": order.Items,
        "UserAddress": user_address,
    }
    
    result = db.orders.insert_one(new_order)
    return get_order(result.inserted_id)


def get_orders(skip: int, limit: int) -> List[OrderInDB]:
    orders = list(db.orders.find().skip(skip).limit(limit))
    orders_with_id = [{"id": str(order.pop("_id")), **order} for order in orders]
    return orders_with_id


def get_order(order_id: str) -> OrderInDB:
    order = db.orders.find_one({"_id": ObjectId(order_id)})
    if order:
        order['id'] = str(order.pop('_id'))
    return order

