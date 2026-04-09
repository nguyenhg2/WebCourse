from fastapi import APIRouter, Depends, HTTPException, status
from app.core.deps import require_role
from app.db.mongo import get_db, serialize_doc, serialize_docs
from app.models.courses import CourseCreate, CourseResponse
from typing import List, Optional
from bson import ObjectId

router = APIRouter()

@router.get("/api/courses", response_model=List[CourseResponse])
async def get_courses(category: Optional[str] = None,db=Depends(get_db)):
    query = {}
    if category:
        query["category"] = category
    courses = await db["courses"].find(query).to_list(length=100)
    return serialize_docs(courses)

@router.get("/api/courses/{course_id}", response_model=CourseResponse)
async def get_course(course_id: str, db=Depends(get_db)):
    course = await db["courses"].find_one({"_id": ObjectId(course_id)})
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy khóa học")
    return serialize_doc(course)

@router.post("/api/courses", response_model=CourseResponse)
async def create_course(payload: CourseCreate, db=Depends(get_db),user=Depends(require_role("admin"))):
    new_course = payload.model_dump()
    result = await db["courses"].insert_one(new_course)
    new_course = await db["courses"].find_one({"_id": result.inserted_id})
    return serialize_doc(new_course)