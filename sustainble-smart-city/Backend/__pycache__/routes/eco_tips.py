from fastapi import APIRouter

router = APIRouter(prefix="/eco", tags=["Eco Tips"])

@router.get("/")
def generate_tip(keyword: str):
    return {
        "tip": f"Reduce your use of {keyword} by opting for reusable alternatives whenever possible!"
    }