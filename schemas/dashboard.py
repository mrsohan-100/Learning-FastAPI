from pydantic import BaseModel


class DashboardStats(BaseModel):
    total_customers: int
    total_products: int
    total_categories: int
    total_invoices: int
    total_revenue: float
