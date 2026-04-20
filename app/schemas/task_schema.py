# from typing_extensions import Self

from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from datetime import date, datetime
from enum import Enum


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str | None
    priority: int
    status: TaskStatus
    due_date: date
    created_at: datetime


class TaskBase(BaseModel):
    title: str = Field(..., min_length=3)
    description: Optional[str] = None
    priority: int = Field(..., ge=1, le=5)
    status: TaskStatus
    due_date: date

    @field_validator("due_date")
    @classmethod
    def validate_due_date(cls, value):
        today = date.today()

        if value <= today:
            raise ValueError("due_date must be in the future")

        return value


class TaskUpdate(TaskBase):
    pass


class TaskCreate(TaskBase):
    pass


# Instead of rewriting everything, we inherit from TaskCreate schema, then add id and created_at fields(DRY)
# class TaskResponse(TaskCreate):
#     id: int
#     created_at: datetime.utcnow()


# Incoming JSON
#     ↓
# Pydantic parsing (types)
#     ↓
# field_validator runs ← YOU are here
#     ↓
# Model created
#     ↓
# FastAPI injects into function
