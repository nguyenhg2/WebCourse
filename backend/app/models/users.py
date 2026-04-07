from pydantic import BaseModel, EmailStr
from app.models.common import Role

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: Role

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int