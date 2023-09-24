from fastapi import APIRouter, Query, Path
from ..models.product import Product
from ..database.products_db import get_products, get_product_by_name, create_product, update_product_by_name
from app.utils.pagination import paginate

router = APIRouter()

@router.get("/products/", response_model=list[Product])
async def list_products(skip: int = Query(0, description="Skip N products", ge=0),
                        limit: int = Query(10, description="Limit the number of products", le=100)):
    products = get_products(skip, limit)
    return paginate(products, skip, limit)

@router.get("/products/{product_name}", response_model=Product)
async def read_product(product_name: str = Path(..., description="Name of the product to retrieve")):
    product = get_product_by_name(product_name)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=Product)
async def create_new_product(product: Product):
    return create_product(product)

@router.put("/products/{product_name}", response_model=Product)
async def update_product_quantity(product_name: str = Path(..., description="Name of the product to update"),
                                  quantity: int = Query(..., description="New available quantity")):
    product = update_product_by_name(product_name, quantity)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
