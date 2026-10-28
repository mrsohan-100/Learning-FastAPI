from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_category():
    return {"message":"Create Category"}


@router.get("/")
async def read_category():
    return {"message":"Read Category"}

@router.get("/{category_id}")
async def read_category():
    return {"message":"Read Category By Id"}


@router.put("/{category_id}")
async def update_category():
    return {"message":"Update Category"}


@router.delete("/{category_id}")
async def delete_category():
    return {"message":"Delete Category"}


