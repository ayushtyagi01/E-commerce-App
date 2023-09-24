from fastapi import APIRouter, Query, Path
from fastapi import FastAPI, HTTPException
from ..models.order import Order, OrderCreate, OrderInResponse
from ..database.orders_db import create_order, get_orders, get_order
from ..utils.pagination import paginate

router = APIRouter()

@router.post("/orders/", response_model=OrderInResponse)  # Use OrderInResponse as the response model
async def create_new_order(order: OrderCreate) -> OrderInResponse:
    # Manually format the UserAddress field
    user_address = {
        "City": order.UserAddress.City,
        "Country": order.UserAddress.Country,
        "ZipCode": order.UserAddress.ZipCode,
    }

    new_order = create_order(order)

    if new_order is None:
        raise HTTPException(status_code=500, detail="Failed to create the order")

    # Wrap the new_order in OrderInResponse
    order_response = OrderInResponse(**new_order, id=str(new_order['_id']))

    return order_response

@router.get("/orders/", response_model=list[OrderInResponse])
async def list_orders(skip: int = Query(0, description="Skip N orders", ge=0),
                      limit: int = Query(10, description="Limit the number of orders", le=100)):
    orders = get_orders(skip, limit)
    print(orders)
    return paginate(orders, skip, limit)

@router.get("/orders/{order_id}", response_model=OrderInResponse)
async def read_order(order_id: str = Path(..., description="ID of the order to retrieve")):
    order = get_order(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
