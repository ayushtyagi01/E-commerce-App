from .connection import db
from ..models.product import Product
from bson import ObjectId

def get_products(skip: int, limit: int):
    skip_count = skip - 1 if skip > 0 else 0
    return list(db.products.find().skip(skip_count).limit(limit))


def get_product_by_name(product_name: str):
    return db.products.find_one({"name": product_name})

def create_product(product: Product):
    result = db.products.insert_one(product.dict())
    return get_product(result.inserted_id)

def update_product_by_name(product_name: str, quantity: int):
    result = db.products.update_one({"name": product_name}, {"$set": {"available_quantity": quantity}})
    if result.modified_count == 0:
        return None
    return get_product_by_name(product_name)
