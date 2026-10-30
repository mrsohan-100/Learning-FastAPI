from sqlalchemy import Session
from schemas.user import (
    LoginRequest,
    RegistrationRequest,
    SendOTPRequest,
    VerifyOTPRequest,
    SetPasswordRequest,
)
from models.user import User

"""
Service is a Function
- DB Session 
- Request Object/Schema->Body,Params
- Model DB Query + Logic 
- Return Result 
"""


def login_user(db: Session, request: LoginRequest):
    pass


def register_user(db: Session, request: RegistrationRequest):
    pass


def send_otp(db: Session, request: SendOTPRequest):
    pass


def verify_otp(db: Session, request: VerifyOTPRequest):
    pass


def set_password(db: Session, request: SetPasswordRequest):
    pass

