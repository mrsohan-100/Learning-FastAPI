from pydantic import BaseModel


class InvoiceCreate(BaseModel):
    customer_id: int
    total: float
    discount: float
    vat: float
    payable: float


class InvoiceUpdate(BaseModel):
    customer_id: int
    total: float
    discount: float
    vat: float
    payable: float
