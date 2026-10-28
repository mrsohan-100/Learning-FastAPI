from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def create_user():
    return {"message":"Create user"}


@router.get("/")
async def read_user():
    return {"message":"Read user"}

@router.get("/{user_id}")
async def read_user():
    return {"message":"Read user By Id"}


@router.put("/{user_id}")
async def update_user():
    return {"message":"Update user"}


@router.delete("/{user_id}")
async def delete_user():
    return {"message":"Delete user"}


@router.put("/update-profile")
async def update_profile():
    return {"message":"Update profile"}
