from datetime import datetime, timezone

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.security import hash_refresh_token, refresh_token_lifetime
from app.models import RefreshToken


def _utc_now_naive() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)


def _is_expired(expires_at: datetime) -> bool:
    if expires_at.tzinfo is not None:
        expires_at = expires_at.replace(tzinfo=None)
    return expires_at <= _utc_now_naive()


async def store_refresh_token(
    user_id: int, token: str, db: AsyncSession
) -> RefreshToken:
    refresh_token = RefreshToken(
        user_id=user_id,
        token_hash=hash_refresh_token(token),
        expires_at=_utc_now_naive() + refresh_token_lifetime(),
    )
    db.add(refresh_token)
    await db.commit()
    await db.refresh(refresh_token)
    return refresh_token


async def get_valid_refresh_token(
    token: str, db: AsyncSession
) -> RefreshToken | None:
    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token_hash == hash_refresh_token(token)
        )
    )
    refresh_token = result.scalar_one_or_none()
    if refresh_token is None:
        return None

    if _is_expired(refresh_token.expires_at):
        await delete_refresh_token_record(refresh_token, db)
        return None

    return refresh_token


async def rotate_refresh_token(
    current_token: RefreshToken, new_token: str, db: AsyncSession
) -> bool:
    """Replace a refresh token record exactly once."""
    result = await db.execute(
        delete(RefreshToken)
        .where(RefreshToken.id == current_token.id)
        .returning(RefreshToken.id)
    )
    if result.scalar_one_or_none() is None:
        await db.rollback()
        return False

    replacement_token = RefreshToken(
        user_id=current_token.user_id,
        token_hash=hash_refresh_token(new_token),
        expires_at=_utc_now_naive() + refresh_token_lifetime(),
    )
    db.add(replacement_token)
    await db.commit()
    return True


async def delete_refresh_token(token: str, db: AsyncSession) -> bool:
    result = await db.execute(
        select(RefreshToken).where(
            RefreshToken.token_hash == hash_refresh_token(token)
        )
    )
    refresh_token = result.scalar_one_or_none()
    if refresh_token is None:
        return False

    await delete_refresh_token_record(refresh_token, db)
    return True


async def delete_refresh_token_record(
    refresh_token: RefreshToken, db: AsyncSession
) -> None:
    await db.delete(refresh_token)
    await db.commit()


async def delete_all_user_refresh_tokens(user_id: int, db: AsyncSession) -> None:
    await db.execute(delete(RefreshToken).where(RefreshToken.user_id == user_id))
    await db.commit()
