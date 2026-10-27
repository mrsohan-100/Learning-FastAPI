from sqlalchemy import Column, BigInteger, String, TIMESTAMP, ForeignKey, Double
from models.base import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, private_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    category_id = Column(BigInteger, ForeignKey("categories.id"), nullable=False)
    name = (Column(String, nullable=False),)
    price = (Column(Double, nullable=False),)
    unit = (Column(String, nullable=False),)
    image_url = (Column(String, nullable=False),)

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
    users = relationship("User", back_populates="product")
    categories = relationship("Category", back_populates="product")
    invoice_products = relationship("InvoiceProduct", back_populates="product")
