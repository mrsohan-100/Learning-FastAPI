from pydantic import BaseModel, EmailStr


class InvoiceProductCreate(BaseModel):
    product_id: int
    invoice_id: int
    qty: float
    sale_price: float


class InvoiceProductUpdate(BaseModel):
    product_id: int
    invoice_id: int
    qty: float
    sale_price: float
