import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.rate_limit import limiter
from app.routers.auth_router import router as auth_router
from app.routers.task_router import router as task_router
from app.routers.user_router import router as user_router
from app.routers.project_router import router as project_router
from app.exceptions import (
    AuthorizationException,
    DatabaseIntegrityException,
    TaskNotFoundException,
)

load_dotenv()

frontend_origins = [
    origin.strip()
    for origin in os.getenv("FRONTEND_ORIGINS", "http://localhost:3000").split(",")
    if origin.strip()
]

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(
    CORSMiddleware,
    allow_origins=frontend_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
app.include_router(task_router)
app.include_router(user_router)
app.include_router(project_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Task API running"}


@app.exception_handler(TaskNotFoundException)
def task_not_found_exception_handler(request: Request, exc: TaskNotFoundException):
    return JSONResponse(status_code=404, content={"detail": exc.message})


@app.exception_handler(DatabaseIntegrityException)
def database_integrity_exception_handler(
    request: Request, exc: DatabaseIntegrityException
):
    return JSONResponse(status_code=409, content={"detail": exc.message})


@app.exception_handler(AuthorizationException)
def authorization_exception_handler(request: Request, exc: AuthorizationException):
    return JSONResponse(status_code=403, content={"detail": exc.message})
