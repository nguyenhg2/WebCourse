from fastapi import APIRouter, Depends
from app.db.mongo import get_db, serialize_docs

router=APIRouter()

@router.get("/api/categories")
async def categories(db=Depends(get_db)):
    categories = await db["courses"].distinct("category")
    return categories