from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import User
from app.schemas.user_schema import UserCreate
from app.auth.security import hash_password


async def create_user(user_data: UserCreate, db: AsyncSession) -> User:
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
    )

    try:
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
    except IntegrityError:
        await db.rollback()
        raise

    return new_user


async def get_all_users(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
) -> list[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return list(result.scalars().all())


async def get_user_by_id(user_id: int, db: AsyncSession) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_user_with_projects(user_id: int, db: AsyncSession) -> User | None:
    result = await db.execute(
        select(User).options(selectinload(User.projects)).where(User.id == user_id)
    )
    return result.scalar_one_or_none()
