from pydantic import BaseModel,EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegistrationRequest(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    mobile: str
    password: str


class SendOTPRequest(BaseModel):
    email: EmailStr



class VerifyOTPRequest(BaseModel):
    email: EmailStr
    otp: str


class SetPasswordRequest(BaseModel):
    email: EmailStr
    otp: str
    password: str


class UserCreate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    mobile: str
    password: str


class UserUpdate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    mobile: str