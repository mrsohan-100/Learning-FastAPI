from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_invoice_item():
    return {"message":"Create invoice item"}


@router.get("/")
async def read_invoice_item():
    return {"message":"Read invoice item"}

@router.get("/{invoice_item_id}")
async def read_invoice_item():
    return {"message":"Read invoice item By Id"}


@router.put("/{invoice_item_id}")
async def update_invoice_item():
    return {"message":"Update invoice item"}


@router.delete("/{invoice_item_id}")
async def delete_invoice_item():
    return {"message":"Delete invoice item"}


