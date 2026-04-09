from fastapi import APIRouter, Depends
from app.db.mongo import get_db, serialize_docs

router=APIRouter()

@router.get("/api/categories")
async def categories(db=Depends(get_db)):
    categories = await db["categories"].find().to_list(length=100)
    return serialize_docs(categories)