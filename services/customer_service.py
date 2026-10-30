from sqlalchemy.orm import Session
from schemas.customer import CustomerCreate, CustomerUpdate
from models.customer import Customer


def create_customer(db: Session, request: CustomerCreate, user_id: int):
    pass


def get_all_customers(db: Session, user_id: int):
    pass


def get_customer_by_id(db: Session, customer_id: int, user_id: int):
    pass


def update_customer(
    db: Session, customer_id: int, request: CustomerUpdate, user_id: int
):
    pass


def delete_customer(db: Session, customer_id: int, user_id: int):
    pass
