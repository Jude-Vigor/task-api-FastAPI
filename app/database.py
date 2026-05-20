from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

load_dotenv()

# 1. THE SINGLETON LAYER (Runs ONCE at startup)
# ==========================================
# This engine object is our Singleton.
# It sets up ONE central pool of connections for the whole app
DATABASE_URL = os.getenv("DATABASE_URL")
DB_ECHO = os.getenv("DB_ECHO", "false").lower() == "true"

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")


engine = create_async_engine(DATABASE_URL, echo=DB_ECHO)
AsyncSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


# 2. THE REQUEST LAYER (Runs on EVERY HTTP request)
# ==========================================


async def get_db():
    # We DO NOT recreate the engine here.
    # We just borrow a quick session from our Singleton engine.
    async with AsyncSessionLocal() as session:
        yield session
