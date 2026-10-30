from sqlalchemy.orm import Session
from schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, request: ProductCreate, user_id: int):
    pass


def get_all_products(db: Session, user_id: int):
    pass


def get_product_by_id(db: Session, product_id: int, user_id: int):
    pass


def update_product(db: Session, product_id: int, request: ProductUpdate, user_id: int):
    pass


def delete_product(db: Session, product_id: int, user_id: int):
    pass