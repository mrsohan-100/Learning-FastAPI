from sqlalchemy.orm import Session
from schemas.invoice import InvoiceCreate, InvoiceUpdate
from schemas.invoice_product import InvoiceProductCreate, InvoiceProductUpdate
from models.invoice import Invoice


def create_invoice(db: Session, request: InvoiceCreate, user_id: int):
    pass


def get_all_invoices(db: Session, user_id: int):
    pass


def get_invoice_by_id(db: Session, invoice_id: int, user_id: int):
    pass


def update_invoice(db: Session, invoice_id: int, request: InvoiceUpdate, user_id: int):
    pass


def delete_invoice(db: Session, invoice_id: int, user_id: int):
    pass


def create_invoice_item(db: Session, request: InvoiceProductCreate, user_id: int):
    pass


def get_all_invoice_items(db: Session, user_id: int):
    pass


def get_invoice_item_by_id(db: Session, invoice_item_id: int, user_id: int):
    pass


def update_invoice_item(
    db: Session, invoice_item_id: int, request: InvoiceProductUpdate, user_id: int
):
    pass


def delete_invoice_item(db: Session, invoice_item_id: int, user_id: int):
    pass
