from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    mobile: str


class CustomerUpdate(BaseModel):
    name: str
    email: EmailStr
    mobile: str
