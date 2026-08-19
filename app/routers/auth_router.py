from fastapi import APIRouter, status, HTTPException, Depends, Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    TokenResponse,
    RefreshTokenRequest,
)
from app.services.user_service import create_user, get_user_by_email, get_user_by_id
from app.services.refresh_token_service import (
    delete_refresh_token,
    get_valid_refresh_token,
    rotate_refresh_token,
    store_refresh_token,
)
from app.auth.dependencies import get_current_user
from app.auth.security import (
    verify_password,
    create_access_token,
    create_refresh_token,
)
from fastapi.security import OAuth2PasswordRequestForm
from app.rate_limit import limiter

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
@limiter.limit("5/minute")
async def register_user(
    request: Request, user_data: UserCreate, db: AsyncSession = Depends(get_db)
):
    try:
        return await create_user(user_data, db)
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists",
        )


@router.post("/login", response_model=TokenResponse)
@limiter.limit("5/minute")
async def login_user(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db),
):
    user = await get_user_by_email(form_data.username, db)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={
            "user_id": user.id,
            "role": user.role,
        },
    )
    refresh_token = create_refresh_token()
    await store_refresh_token(user.id, refresh_token, db)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.post("/refresh", response_model=TokenResponse)
@limiter.limit("5/minute")
async def refresh_tokens(
    request: Request,
    refresh_data: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db),
):
    stored_refresh_token = await get_valid_refresh_token(
        refresh_data.refresh_token, db
    )
    if stored_refresh_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    user = await get_user_by_id(stored_refresh_token.user_id, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    access_token = create_access_token(
        data={"user_id": user.id, "role": user.role}
    )
    new_refresh_token = create_refresh_token()
    was_rotated = await rotate_refresh_token(
        stored_refresh_token, new_refresh_token, db
    )
    if not was_rotated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
        )

    return {
        "access_token": access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
@limiter.limit("5/minute")
async def logout_user(
    request: Request,
    refresh_data: RefreshTokenRequest,
    db: AsyncSession = Depends(get_db),
):
    await delete_refresh_token(refresh_data.refresh_token, db)
    return None


@router.get("/me", response_model=UserResponse)
@limiter.limit("5/minute")
async def read_current_user(request: Request, current_user=Depends(get_current_user)):
    return current_user
