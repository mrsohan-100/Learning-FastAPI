from sqlalchemy.orm import Session
from schemas.category import CategoryCreate, CategoryUpdate
from models.category import Category


def create_category(db: Session, request: CategoryCreate, user_id: int):
    pass


def get_all_categories(db: Session, user_id: int):
    pass


def get_category_by_id(db: Session, category_id: int, user_id: int):
    pass


def update_category(
    db: Session, category_id: int, request: CategoryUpdate, user_id: int
):
    pass


def delete_category(db: Session, category_id: int, user_id: int):
    pass
