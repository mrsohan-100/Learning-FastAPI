from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserUpdate


def create_user(db: Session, request: UserCreate):
    pass


def get_all_users(db: Session):
    pass


def get_user_by_id(db: Session, user_id: int):
    pass


def update_user(db: Session, user_id: int, request: UserUpdate):
    pass


def delete_user(db: Session, user_id: int):
    pass


def update_profile(db: Session, user_id: int, request: UserUpdate):
    pass