from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from app.schemas.task_schema import TaskResponse, TaskWithAssigneeResponse


class ProjectCreate(BaseModel):
    # Reject unknown request fields instead of silently ignoring them.
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=3, max_length=120)
    description: str | None = Field(None, max_length=500)
    owner_id: int = Field(..., ge=1)


class ProjectUpdate(BaseModel):
    # Reject unknown request fields instead of silently ignoring them.
    model_config = ConfigDict(extra="forbid")

    name: str = Field(..., min_length=3, max_length=120)
    description: str | None = Field(None, max_length=500)


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    owner_id: int
    created_at: datetime


class ProjectWithTaskCountResponse(ProjectResponse):
    task_count: int


class ProjectWithTasksResponse(ProjectResponse):
    tasks: list[TaskWithAssigneeResponse]
