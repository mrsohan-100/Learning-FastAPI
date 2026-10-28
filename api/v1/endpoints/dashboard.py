from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_dashboard():
    return {"message":"Dashboard"}


@router.get("/stats")
async def get_dashboard_stats():
    return {"message":"Dashboard Stats"}

@router.get("/recent-activities")
async def get_recent_acitivities():
    return {"message":"Recent Activities"}






