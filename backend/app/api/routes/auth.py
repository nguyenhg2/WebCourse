from fastapi import APIRouter, HTTPException
from app.models.users import LoginRequest, RegisterRequest, TokenResponse
from app.core.security import create_access_token, get_password_hash, verify_password
from app.db.mongo import get_db, serialize_doc
from datetime import timedelta
from app.core.config import settings

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
    db=get_db()
    user=await db.users.find_one({"email": payload.email})
    if not user:
        raise HTTPException(status_code=400, detail="Email hoặc mật khẩu không đúng")
    if not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Email hoặc mật khẩu không đúng")
    
    user=serialize_doc(user)
    token=create_access_token(
        {
            "user_id": user["_id"],
            "email": user["email"],
            "role": user["role"]
        },
        expires_delta=timedelta(minutes=settings.access_token_expire_minutes),
    )
    return TokenResponse(access_token=token, expires_in=settings.access_token_expire_minutes * 60)
