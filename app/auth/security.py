import os
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

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return None
