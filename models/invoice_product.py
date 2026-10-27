from sqlalchemy import Column, BigInteger, String, TIMESTAMP, ForeignKey, Double
from models.base import Base
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class InvoiceProduct(Base):
    __tablename__ = "invoice_products"

    id = Column(BigInteger, private_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    product_id = Column(BigInteger, ForeignKey("products.id"), nullable=False)
    invoice_id = Column(BigInteger, ForeignKey("invoices.id"), nullable=False)
    qty = Column(Double, nullable=False),
    sale_price = Column(Double, nullable=False),

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
    users = relationship("User", back_populates="invoice_product")
    products = relationship("Product", back_populates="invoice_product")
    invoices = relationship("Invoice", back_populates="invoice_product")
