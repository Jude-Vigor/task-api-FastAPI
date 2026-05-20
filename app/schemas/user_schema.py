from pydantic import EmailStr, BaseModel, Field, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    # Reject unknown request fields instead of silently ignoring them.
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=3, max_length=80)
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: datetime
