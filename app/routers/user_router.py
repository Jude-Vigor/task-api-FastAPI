from fastapi import APIRouter, status, HTTPException, Depends, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.project_schema import ProjectResponse
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_all_users,
    get_user_by_id,
    get_user_with_projects,
)
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
async def register_user(user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    try:
        return await create_user(user_data, db)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        )


@router.get("/", response_model=List[UserResponse])
async def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db),
):
    return await get_all_users(db, skip, limit)


@router.get("/{user_id}", response_model=UserResponse)
async def get_single_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    user = await get_user_by_id(user_id, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user


@router.get("/{user_id}/projects", response_model=List[ProjectResponse])
async def get_projects_for_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):
    user = await get_user_with_projects(user_id, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found",
        )

    return user.projects
