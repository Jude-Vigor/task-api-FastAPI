from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.security import oauth2_scheme, verify_token
from app.database import get_db
from app.models import User
from app.services.user_service import get_user_by_id
from app.schemas.user_schema import UserRole
from app.auth.permissions import Action, PERMISSIONS, Resource


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = verify_token(token)
    if payload is None:
        raise credentials_exception

    user_id = payload.get("user_id")
    if user_id is None:
        raise credentials_exception

    user = await get_user_by_id(user_id, db)
    if user is None:
        raise credentials_exception

    return user


def require_role(*allowed_roles: UserRole):
    async def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Not permitted"
            )
        return current_user

    return role_checker


def require_permission(resource: Resource, action: Action):
    async def permission_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        role = UserRole(current_user.role)
        allowed_actions = PERMISSIONS.get(role, {}).get(resource, set())

        if action not in allowed_actions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not permitted",
            )

        return current_user

    return permission_checker
