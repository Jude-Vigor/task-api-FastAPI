from pydantic import EmailStr, BaseModel, Field, field_validator, ConfigDict
from datetime import datetime
from enum import Enum


class UserCreate(BaseModel):
    # Reject unknown request fields instead of silently ignoring them.
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=3, max_length=80)
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, pwd: str):
        if len(pwd) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(char.isdigit() for char in pwd):
            raise ValueError("Password must contain at least one number")
        return pwd

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower()


class UserRole(str, Enum):
    admin = "admin"
    manager = "manager"
    member = "member"


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email")
    def normalize_email(cls, v):
        return v.lower()


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
