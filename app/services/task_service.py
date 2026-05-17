from app.schemas.task_schema import TaskCreate, TaskUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Task
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, or_
from app.exceptions import DatabaseIntegrityException


async def create_task(task_data: TaskCreate, db: AsyncSession) -> Task:
    new_task = Task(
        title=task_data.title,
        description=task_data.description,
        status=task_data.status.value,
        priority=task_data.priority,
        due_date=task_data.due_date,
    )
    try:
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)
        print("TASKS AFTER CREATE:", new_task)
    except IntegrityError:
        await db.rollback()
        raise DatabaseIntegrityException(
            "Task could not be saved because of a database constraint"
        )
    return new_task


async def get_all_tasks(
    db: AsyncSession,
    status=None,
    priority=None,
    search=None,
    skip: int = 0,
    limit: int = 10,
    sort_by=None,
    order: str = "asc",
):
    query = select(Task)

    if status:
        query = query.where(Task.status == status.value)

    if priority is not None:
        query = query.where(Task.priority == priority)

    if search:
        search_pattern = f"%{search}%"
        query = query.where(
            or_(
                Task.title.ilike(search_pattern),
                Task.description.ilike(search_pattern),
            )
        )

    if sort_by:
        sort_column = getattr(Task, sort_by)

        if order == "desc":
            query = query.order_by(sort_column.desc())
        else:
            query = query.order_by(sort_column.asc())

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)
    print("INSIDE get_all_tasks")

    return result.scalars().all()


async def get_task_by_id(task_id: int, db: AsyncSession):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()


async def update_task(task_id: int, task_data: TaskUpdate, db: AsyncSession):
    task = await get_task_by_id(task_id, db)

    if not task:
        return None

    task.title = task_data.title
    task.description = task_data.description
    task.priority = task_data.priority
    task.status = task_data.status.value
    task.due_date = task_data.due_date

    try:
        await db.commit()
        await db.refresh(task)
    except IntegrityError:
        await db.rollback()
        raise DatabaseIntegrityException(
            "Task could not be updated because of a database constraint"
        )

    return task


async def delete_task(task_id: int, db: AsyncSession):
    task = await get_task_by_id(task_id, db)

    if not task:
        return None
    try:
        await db.delete(task)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise DatabaseIntegrityException(
            "Task could not be deleted because of a database constraint"
        )
    return task
