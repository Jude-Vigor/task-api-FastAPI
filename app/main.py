from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routers.auth_router import router as auth_router
from app.routers.task_router import router as task_router
from app.routers.user_router import router as user_router
from app.routers.project_router import router as project_router
from app.exceptions import (
    AuthorizationException,
    DatabaseIntegrityException,
    TaskNotFoundException,
)

app = FastAPI()
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
