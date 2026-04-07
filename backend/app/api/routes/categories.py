from fastapi import APIRouter

router=APIRouter()

@router.get("/api/categories")
async def categories():
    return {"categories": ["Programming", "Design", "Marketing", "Business"]}