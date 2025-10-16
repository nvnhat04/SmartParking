from fastapi import APIRouter

router = APIRouter(
    prefix="/parking",
    tags=["Parking System"]
)

@router.get("/status")
def get_status():
    return {"parking_status": "available", "slots_free": 12}
