from fastapi import APIRouter
from .endpoints import (
    auth,
    categories,
    customers,
    dashboard,
    invoice_item,
    invoices,
    products,
    users,
)

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(categories.router, prefix="/categories", tags=["Categories"])
router.include_router(customers.router, prefix="/customers", tags=["Customers"])
router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
router.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
router.include_router(invoice_item.router, prefix="/invoice-item", tags=["Invoice_Item"])
router.include_router(invoices.router, prefix="/invoices", tags=["Invoices"])
router.include_router(products.router, prefix="/products", tags=["Products"])
router.include_router(users.router, prefix="/users", tags=["Users"])
