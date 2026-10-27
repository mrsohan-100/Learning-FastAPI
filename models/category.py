from sqlalchemy import Column, BigInteger, String, TIMESTAMP, ForeignKey
from models.base import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(BigInteger, private_key=True, autoincrement=True)
    name = (Column(String, nullable=False),)
    user_id = (Column(BigInteger, ForeignKey("users.id"), nullable=False),)
    create_at = Column(
        TIMESTAMP, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    # relationship
    users = relationship("User", back_populates="category")
    products = relationship("Product", back_populates="category")
