from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_product():
    return {"message":"Create product"}


@router.get("/")
async def read_product():
    return {"message":"Read product"}

@router.get("/{product_id}")
async def read_product():
    return {"message":"Read product By Id"}


@router.put("/{product_id}")
async def update_product():
    return {"message":"Update product"}


@router.delete("/{product_id}")
async def delete_product():
    return {"message":"Delete product"}


