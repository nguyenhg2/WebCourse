from fastapi import APIRouter
from app.models.users import LoginRequest, RegisterRequest, TokenResponse

router=APIRouter()
@router.post("/api/auth/register", response_model=RegisterRequest)
async def register(payload: RegisterRequest):
    return payload

@router.post("/api/auth/login", response_model=TokenResponse)
async def login(payload: LoginRequest):
    return payload