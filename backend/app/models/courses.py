from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: str
    thumbnail: Optional[str] = None
    price: float = 0.0
    category: str
    rating: float = 0.0

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    thumbnail: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    

class CourseResponse(CourseBase):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True