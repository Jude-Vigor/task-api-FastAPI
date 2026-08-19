import asyncio
from datetime import date, timedelta

from sqlalchemy import select

from app.auth.security import hash_password
from app.database import AsyncSessionLocal
from app.models import Project, Task, User

SEED_PASSWORD = "Password1"

USERS = [
    {
        "name": "Admin User",
        "email": "admin@example.com",
        "role": "admin",
    },
    {"name": "Amina Bello", "email": "amina.bello@example.com", "role": "member"},
    {"name": "Ben Carter", "email": "ben.carter@example.com", "role": "member"},
    {"name": "Chloe Singh", "email": "chloe.singh@example.com", "role": "manager"},
    {"name": "Diego Ramos", "email": "diego.ramos@example.com", "role": "member"},
]

PROJECTS = [
    {
        "name": "Customer Portal API",
        "description": "Backend API for customer profiles, projects, and task tracking.",
        "owner_email": "chloe.singh@example.com",
    },
    {
        "name": "Inventory Automation",
        "description": "Internal service for stock updates and warehouse task workflows.",
        "owner_email": "ben.carter@example.com",
    },
    {
        "name": "Analytics Dashboard",
        "description": "Reporting backend for operational metrics and team delivery insights.",
        "owner_email": "amina.bello@example.com",
    },
]

TASKS = [
    {
        "title": "Design user project relationships",
        "description": "Map user, project, and task ownership rules for the API.",
        "status": "done",
        "priority": 4,
        "due_in_days": 4,
        "project_name": "Customer Portal API",
        "assignee_email": "amina.bello@example.com",
    },
    {
        "title": "Add project task-count query",
        "description": "Return project summaries with task_count using SQL aggregation.",
        "status": "in_progress",
        "priority": 5,
        "due_in_days": 7,
        "project_name": "Customer Portal API",
        "assignee_email": "ben.carter@example.com",
    },
    {
        "title": "Validate duplicate user emails",
        "description": "Handle unique email conflicts with a clean API response.",
        "status": "pending",
        "priority": 3,
        "due_in_days": 10,
        "project_name": "Customer Portal API",
        "assignee_email": "diego.ramos@example.com",
    },
    {
        "title": "Create warehouse sync endpoint",
        "description": "Draft the endpoint contract for inventory sync jobs.",
        "status": "pending",
        "priority": 4,
        "due_in_days": 6,
        "project_name": "Inventory Automation",
        "assignee_email": "chloe.singh@example.com",
    },
    {
        "title": "Review failed stock imports",
        "description": "Add task records for import failures that need manual review.",
        "status": "in_progress",
        "priority": 2,
        "due_in_days": 12,
        "project_name": "Inventory Automation",
        "assignee_email": "ben.carter@example.com",
    },
    {
        "title": "Model dashboard metrics",
        "description": "Define the first report queries for project health and overdue work.",
        "status": "pending",
        "priority": 5,
        "due_in_days": 8,
        "project_name": "Analytics Dashboard",
        "assignee_email": "amina.bello@example.com",
    },
    {
        "title": "Seed demo reporting data",
        "description": "Create realistic records for testing dashboard responses.",
        "status": "pending",
        "priority": 3,
        "due_in_days": 14,
        "project_name": "Analytics Dashboard",
        "assignee_email": "diego.ramos@example.com",
    },
]


async def get_or_create_user(db, user_data: dict) -> User:
    result = await db.execute(select(User).where(User.email == user_data["email"]))
    user = result.scalar_one_or_none()

    password_hash = hash_password(SEED_PASSWORD)

    if user:
        if not user.password_hash:
            user.password_hash = password_hash
        return user

    user = User(
        name=user_data["name"],
        email=user_data["email"],
        role=user_data["role"],
        password_hash=password_hash,
    )
    db.add(user)
    await db.flush()
    return user


async def get_or_create_project(
    db,
    project_data: dict,
    users_by_email: dict[str, User],
) -> Project:
    result = await db.execute(
        select(Project).where(Project.name == project_data["name"])
    )
    project = result.scalar_one_or_none()

    if project:
        return project

    owner = users_by_email[project_data["owner_email"]]
    project = Project(
        name=project_data["name"],
        description=project_data["description"],
        owner_id=owner.id,
    )
    db.add(project)
    await db.flush()
    return project


async def task_exists(db, title: str, project_id: int) -> bool:
    result = await db.execute(
        select(Task).where(Task.title == title, Task.project_id == project_id)
    )
    return result.scalar_one_or_none() is not None


async def seed_database() -> None:
    async with AsyncSessionLocal() as db:
        users_by_email = {}
        for user_data in USERS:
            user = await get_or_create_user(db, user_data)
            users_by_email[user.email] = user

        projects_by_name = {}
        for project_data in PROJECTS:
            project = await get_or_create_project(db, project_data, users_by_email)
            projects_by_name[project.name] = project

        created_task_count = 0
        for task_data in TASKS:
            project = projects_by_name[task_data["project_name"]]
            if await task_exists(db, task_data["title"], project.id):
                continue

            assignee = users_by_email[task_data["assignee_email"]]
            task = Task(
                title=task_data["title"],
                description=task_data["description"],
                status=task_data["status"],
                priority=task_data["priority"],
                due_date=date.today() + timedelta(days=task_data["due_in_days"]),
                owner_id=assignee.id,
                project_id=project.id,
            )
            db.add(task)
            created_task_count += 1

        await db.commit()

        print("Seed complete")
        print(f"Users available: {len(users_by_email)}")
        print(f"Projects available: {len(projects_by_name)}")
        print(f"New tasks created: {created_task_count}")
        print(f"All seed users password: {SEED_PASSWORD}")


if __name__ == "__main__":
    asyncio.run(seed_database())
