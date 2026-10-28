from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_invoice():
    return {"message":"Create invoice"}


@router.get("/")
async def read_invoice():
    return {"message":"Read invoice"}

@router.get("/{invoice_id}")
async def read_invoice():
    return {"message":"Read invoice By Id"}


@router.put("/{invoice_id}")
async def update_invoice():
    return {"message":"Update invoice"}


@router.delete("/{invoice_id}")
async def delete_invoice():
    return {"message":"Delete invoice"}


