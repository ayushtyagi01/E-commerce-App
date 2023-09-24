from fastapi import FastAPI
from app.api import products, orders

app = FastAPI()
# @router.post("/products/", response_model=Product)
# async def create_new_product(product: Product):
#     return create_product(product)

# Include API routers
app.include_router(products.router)
app.include_router(orders.router)
# app.include_router(users.router)  # Include only if you have a users API

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
