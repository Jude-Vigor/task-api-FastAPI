from fastapi import APIRouter, status, Response, Query, Depends, HTTPException
from app.schemas.task_schema import (
    TaskAssign,
    TaskCreate,
    TaskUpdate,
    TaskStatus,
    TaskResponse,
)
from app.services.task_service import (
    assign_task,
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
)
from typing import List
from app.exceptions import TaskNotFoundException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.auth.dependencies import require_permission, require_role
from app.auth.permissions import Action, Resource
from app.schemas.user_schema import UserRole
from app.models import User

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[TaskResponse])
async def get_tasks(
    status: TaskStatus | None = None,
    priority: int | None = Query(None, ge=1, le=5),
    search: str | None = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str | None = Query(None, pattern="^(id|title|priority|status|due_date)$"),
    order: str = Query("asc", pattern="^(asc|desc)$"),
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_permission(Resource.tasks, Action.read)),
):
    return await get_all_tasks(
        db, current_user, status, priority, search, skip, limit, sort_by, order
    )


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TaskResponse)
async def add_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_permission(Resource.tasks, Action.create)),
):
    created_task, error = await create_task(task, db, current_user.id)

    if error == "owner_not_found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Authenticated user not found",
        )

    if error == "project_not_found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with id {task.project_id} not found",
        )

    return created_task


@router.get("/{task_id}", response_model=TaskResponse)
async def get_single_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_permission(Resource.tasks, Action.read)),
):
    task = await get_task_by_id(task_id, db, current_user)

    if not task:
        raise TaskNotFoundException(task_id)
    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_single_task(
    task_id: int,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_permission(Resource.tasks, Action.update)),
):
    updated_task = await update_task(task_id, task, db, current_user)

    if not updated_task:
        raise TaskNotFoundException(task_id)
    return updated_task


@router.patch("/{task_id}/assign", response_model=TaskResponse)
async def assign_single_task(
    task_id: int,
    assignment_data: TaskAssign,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_permission(Resource.tasks, Action.assign)),
    _: User = Depends(require_role(UserRole.admin, UserRole.manager)),
):
    assigned_task, error = await assign_task(
        task_id, assignment_data, db, current_user
    )

    if error == "task_not_found":
        raise TaskNotFoundException(task_id)

    if error == "assignee_not_found":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {assignment_data.assignee_id} not found",
        )

    return assigned_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_single_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(require_permission(Resource.tasks, Action.delete)),
):
    deleted = await delete_task(task_id, db, current_user)

    if not deleted:
        raise TaskNotFoundException(task_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
