from fastapi import APIRouter

router=APIRouter()
@router.get("/api/courses")
async def get_courses():
    return {"message": "Danh sách khóa học"}