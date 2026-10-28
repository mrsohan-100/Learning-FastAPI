from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"message":"Login"}

@router.post("/registration")
async def registration():
    return {"message":"Registration"}

@router.post("/send-otp")
async def send_otp():
    return {"message":"Send Otp"}

@router.post("/verify-otp")
async def verify_otp():
    return {"message":"Verify Otp"}

@router.post("/setpass")
async def setpass():
    return {"message":"Set Pass"}
