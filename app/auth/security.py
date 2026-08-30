import hashlib
import os
import secrets
from datetime import datetime, timedelta, timezone
from typing import cast
import jwt
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext

load_dotenv()


ALGORITHM = cast(str, os.getenv("JWT_ALGORITHM", "HS256"))
SECRET_KEY = cast(str, os.getenv("JWT_SECRET_KEY"))
if not SECRET_KEY or not ALGORITHM:
    raise RuntimeError("JWT_SECRET_KEY or ALG is not set")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "10"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))

# Swagger will expect a login flow at the "/login" path
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def access_token_lifetime() -> timedelta:
    return timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


def refresh_token_lifetime() -> timedelta:
    return timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta if expires_delta is not None else access_token_lifetime()
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token() -> str:
    return secrets.token_urlsafe(32)


def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def verify_refresh_token(plain_token: str, stored_hash: str) -> bool:
    return secrets.compare_digest(hash_refresh_token(plain_token), stored_hash)


def verify_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return None
