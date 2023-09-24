from pymongo import MongoClient

# Database setup and configuration
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]
product_collection = db["products"]
order_collection = db["orders"]

# You can define database-related functions here, such as database queries and data manipulation
