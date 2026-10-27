from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from models.base import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, private_key=True, autoincrement=True)
    first_name = (Column(String, nullable=False),)
    last_name = (Column(String, nullable=False),)
    email = (Column(String, unique=True, nullable=False),)
    mobile = (Column(String, nullable=False),)
    password = (Column(String, nullable=False),)
    otp = (Column(String, nullable=False),)
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
    categories = relationship("Category", back_populates="user")
    products = relationship("Product", back_populates="user")
    invoices = relationship("Invoice", back_populates="user")
    invoice_products = relationship("InvoiceProduct", back_populates="user")
    customers = relationship("Customer", back_populates="user")
