from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import Project, Task, User
from app.schemas.project_schema import ProjectCreate, ProjectUpdate
from app.schemas.user_schema import UserRole


async def create_project(
    project_data: ProjectCreate,
    db: AsyncSession,
    owner_id: int,
) -> Project | None:
    owner_result = await db.execute(select(User).where(User.id == owner_id))
    owner = owner_result.scalar_one_or_none()

    if not owner:
        return None

    new_project = Project(
        name=project_data.name,
        description=project_data.description,
        owner_id=owner_id,
    )

    try:
        db.add(new_project)
        await db.commit()
        await db.refresh(new_project)
    except IntegrityError:
        await db.rollback()
        raise

    return new_project


async def get_all_projects(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> list[dict]:
    result = await db.execute(
        select(Project, func.count(Task.id).label("task_count"))
        .outerjoin(Task, Task.project_id == Project.id)
        .group_by(Project.id)
        .offset(skip)
        .limit(limit)
    )

    projects = []
    for project, task_count in result.all():
        projects.append(
            {
                "id": project.id,
                "name": project.name,
                "description": project.description,
                "owner_id": project.owner_id,
                "created_at": project.created_at,
                "task_count": task_count,
            }
        )

    return projects


async def get_project_by_id(project_id: int, db: AsyncSession) -> Project | None:
    result = await db.execute(
        select(Project)
        .options(selectinload(Project.tasks))
        .where(Project.id == project_id)
    )
    return result.scalar_one_or_none()


async def get_project_with_tasks_and_assignees(
    project_id: int,
    db: AsyncSession,
) -> dict | None:
    result = await db.execute(
        select(Project)
        .options(selectinload(Project.tasks).selectinload(Task.owner))
        .where(Project.id == project_id)
    )
    project = result.scalar_one_or_none()

    if not project:
        return None

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "owner_id": project.owner_id,
        "created_at": project.created_at,
        "tasks": [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "priority": task.priority,
                "status": task.status,
                "due_date": task.due_date,
                "owner_id": task.owner_id,
                "project_id": task.project_id,
                "created_at": task.created_at,
                "assignee": task.owner,
            }
            for task in project.tasks
        ],
    }


async def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: AsyncSession,
) -> Project | None:
    project = await get_project_by_id(project_id, db)

    if not project:
        return None

    project.name = project_data.name
    project.description = project_data.description

    try:
        await db.commit()
        await db.refresh(project)
    except IntegrityError:
        await db.rollback()
        raise

    return project


async def delete_project(
    project_id: int,
    db: AsyncSession,
    current_user: User,
) -> Project | None:
    project = await get_project_by_id(project_id, db)

    if not project:
        return None

    if current_user.role != UserRole.admin and project.owner_id != current_user.id:
        return None

    try:
        await db.delete(project)
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise

    return project
