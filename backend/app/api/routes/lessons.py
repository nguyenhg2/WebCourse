from fastapi import APIRouter, Depends
from app.db.mongo import get_db, serialize_doc

router=APIRouter()

@router.get("/api/courses/{course_id}/lessons")
async def get_lessons(course_id: str, db=Depends(get_db)):
    lessons = await db["lessons"].find({"course_id": course_id}).to_list(length=None)
    return [serialize_doc(lesson) for lesson in lessons]
