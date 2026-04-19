from fastapi import APIRouter, status, HTTPException, Response, Query
from app.schemas.task_schema import TaskCreate, TaskUpdate, TaskStatus
from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
def get_tasks(
    status: TaskStatus | None = None,
    priority: int | None = Query(None, ge=1, le=5),
    search: str | None = None,
    sort_by: str | None = Query(None, pattern="^(id|title|priority|status|due_date)$"),
    order: str = Query("asc", pattern="^(asc|desc)$"),
):
    print("GET /tasks endpoint hit")
    return get_all_tasks(status, priority, search, sort_by, order)


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate):
    print("POST /tasks endpoint hit")
    return create_task(task)


@router.get("/{task_id}")
def get_single_task(task_id: int):
    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}")
def update_single_task(task_id: int, task: TaskUpdate):
    updated_task = update_task(task_id, task)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_single_task(task_id: int):
    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
