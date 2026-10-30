from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    unit: str
    category_id: int
    img_url: str | None = None


class ProductUpdate(BaseModel):
    name: str
    price: float
    unit: str
    category_id: int
    img_url: str | None = None
