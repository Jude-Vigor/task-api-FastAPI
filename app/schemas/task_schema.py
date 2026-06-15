# from typing_extensions import Self

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Optional
from datetime import date, datetime
from enum import Enum

from app.schemas.user_schema import UserResponse


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
    owner_id: int
    project_id: int
    created_at: datetime


class TaskWithAssigneeResponse(TaskResponse):
    assignee: UserResponse


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
    # Reject unknown request fields instead of silently ignoring them.
    model_config = ConfigDict(extra="forbid")

    project_id: int = Field(..., ge=1)


class TaskAssign(BaseModel):
    # Reject unknown request fields instead of silently ignoring them.
    model_config = ConfigDict(extra="forbid")

    assignee_id: int = Field(..., ge=1)


# Incoming JSON
#     ↓
# Pydantic parsing (types)
#     ↓
# field_validator runs ← YOU are here
#     ↓
# Model created
#     ↓
# FastAPI injects into function
