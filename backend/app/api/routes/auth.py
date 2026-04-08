from fastapi import APIRouter, HTTPException
from app.models.users import LoginRequest, RegisterRequest, TokenResponse
from app.core.security import get_password_hash
from app.db.mongo import get_db

router=APIRouter()
@router.post("/api/auth/register")
async def register(payload: RegisterRequest):
    db=get_db()
    user_email=payload.email
    if (await db.users.find_one({"email": user_email})):
        raise HTTPException(status_code=400, detail="Email đã được đăng ký")
    hashed_pwd=get_password_hash(payload.password)
    user_doc={
        "name": payload.name,
        "email": user_email,
        "hashed_password": hashed_pwd,
        "role": "student"
    }
    await db.users.insert_one(user_doc)
    return {"message": "Đăng ký thành công"}

@router.post("/api/auth/login", response_model=TokenResponse)
async def login(payload: LoginRequest):
    return payload