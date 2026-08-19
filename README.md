# Project Management API

A FastAPI backend for managing users, projects, and tasks with PostgreSQL persistence and JWT-based authentication.

This project started as a task CRUD API and now uses async SQLAlchemy, Alembic migrations, relational data modeling, JWT access tokens, refresh-token rotation, role-based access control, rate limiting, and CORS configuration.

## Features

- User CRUD
  - List users
  - Get user by ID
  - Get a user's projects
- Auth and security
  - Register and login users
  - Short-lived JWT access tokens
  - Long-lived refresh tokens stored as hashes
  - Refresh-token rotation
  - Logout by revoking refresh tokens
  - Role-based access control
  - Auth endpoint rate limiting
  - CORS restricted to configured frontend origins
- Project CRUD
  - Create projects
  - List projects with `task_count`
  - Get a project with tasks and assignee details
  - Update projects
  - Delete projects
- Task CRUD
  - Create, read, update, and delete tasks
  - Assign tasks to users
  - Filter by status and priority
  - Search by title or description
  - Sort and paginate results
- PostgreSQL-backed persistence
- Async SQLAlchemy database access
- Alembic database migrations
- Pydantic request and response validation
- Seed script with realistic demo data

## Tech Stack

- Python
- FastAPI
- Pydantic
- PostgreSQL
- SQLAlchemy async ORM
- asyncpg
- Alembic
- Uvicorn
- JWT
- Passlib bcrypt
- SlowAPI

## Project Structure

```text
app/
|-- main.py
|-- database.py
|-- models.py
|-- exceptions.py
|-- seed.py
|-- rate_limit.py
|-- auth/
|   |-- dependencies.py
|   |-- permissions.py
|   |-- security.py
|-- routers/
|   |-- auth_router.py
|   |-- task_router.py
|   |-- user_router.py
|   |-- project_router.py
|-- schemas/
|   |-- task_schema.py
|   |-- user_schema.py
|   |-- project_schema.py
|-- services/
|   |-- task_service.py
|   |-- user_service.py
|   |-- project_service.py
alembic/
|-- env.py
|-- versions/
assets/
|-- screenshots and test evidence
alembic.ini
requirements.txt
README.md
```

## Database Model


users
|-- id
|-- name
|-- email
|-- password_hash
|-- role
|-- created_at

projects
|-- id
|-- name
|-- description
|-- owner_id -> users.id
|-- created_at

tasks
|-- id
|-- title
|-- description
|-- status
|-- priority
|-- due_date
|-- owner_id -> users.id
|-- project_id -> projects.id
|-- created_at

refresh_tokens
|-- id
|-- user_id -> users.id
|-- token_hash
|-- expires_at
|-- created_at
```

Relationships:

```
User -> Projects
User -> Assigned Tasks
Project -> Tasks
Task -> Assignee/User
```

## Setup

### 1. Clone the repository

```powershell
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd backend_learning
```

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Create a PostgreSQL database

Create a local PostgreSQL database. Example name:

```
fastapi_db
```

You can create it with pgAdmin or with `psql`:

```sql
CREATE DATABASE fastapi_db;
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+asyncpg://postgres:YOUR_PASSWORD@localhost:5432/fastapi_db
DB_ECHO=false
JWT_SECRET_KEY=replace_with_a_long_random_secret
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
FRONTEND_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

Replace `postgres`, `YOUR_PASSWORD`, host, port, or database name with your local PostgreSQL settings.
Set `DB_ECHO=true` only when you want SQLAlchemy to print SQL queries while debugging.
Use a strong `JWT_SECRET_KEY` in production.

### 6. Run migrations

```powershell
.\venv\Scripts\python.exe -m alembic upgrade head
```

This creates the database tables and relationships.

### 7. Seed the database

```powershell
.\venv\Scripts\python.exe -m app.seed
```

The seed script creates realistic users, projects, and tasks. It is safe to rerun because it checks for existing seed records before creating new ones.

Seed accounts:

```text
admin@example.com          role: admin
chloe.singh@example.com    role: manager
amina.bello@example.com    role: member
ben.carter@example.com     role: member
diego.ramos@example.com    role: member
```

All seed users use this password:

```text
Password1
```

### 8. Run the server

```powershell
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Auth

```http
POST /auth/register
POST /auth/login
POST /auth/refresh
POST /auth/logout
GET /auth/me
```

### Users

```http
GET /users/
GET /users/{user_id}
GET /users/{user_id}/projects
```

### Projects

```http
POST /projects/
GET /projects/
GET /projects/{project_id}
PUT /projects/{project_id}
DELETE /projects/{project_id}
```

`GET /projects/` returns each project with a `task_count`.

`GET /projects/{project_id}` returns the project with tasks and each task's assignee details.

### Tasks

```http
POST /tasks/
GET /tasks/
GET /tasks/{task_id}
PUT /tasks/{task_id}
PATCH /tasks/{task_id}/assign
DELETE /tasks/{task_id}
```

Task assignment request body:

```json
{
  "assignee_id": 1
}
```

## Authentication

### Register

Create a user with:

```http
POST /auth/register
```

Request body:

```json
{
  "name": "Amina Bello",
  "email": "amina@example.com",
  "password": "Password1"
}
```

New users are created as `member` by default. Public registration does not allow clients to choose their own role.

### Login

Login uses OAuth2 password form data:

```http
POST /auth/login
```

Form fields:

```text
username=admin@example.com
password=Password1
```

Successful login returns:

```json
{
  "access_token": "jwt_access_token",
  "refresh_token": "random_refresh_token",
  "token_type": "bearer"
}
```

The access token expires quickly, by default after 15 minutes. The refresh token lasts longer, by default 7 days, and is stored in the database as a hash.

### Use Protected Routes

Send the access token in the `Authorization` header:

```http
Authorization: Bearer jwt_access_token
```

In Swagger UI, click `Authorize`, enter the login `username` and `password`, then close the modal. Swagger calls `/auth/login` and stores the access token for protected endpoints.

### Refresh Tokens

When the access token expires, request a new token pair:

```http
POST /auth/refresh
```

Request body:

```json
{
  "refresh_token": "current_refresh_token"
}
```

The API returns a new access token and a new refresh token. The old refresh token is deleted from the database during rotation, so it cannot be reused.

### Logout

Logout revokes the refresh token:

```http
POST /auth/logout
```

Request body:

```json
{
  "refresh_token": "current_refresh_token"
}
```

Successful logout returns `204 No Content`. Existing access tokens may continue working until they expire, but the revoked refresh token can no longer create new access tokens.

## Role Permissions

The API uses role-based access control through `admin`, `manager`, and `member` roles.

| Role | Permissions |
| --- | --- |
| `admin` | Can read users, manage all projects, manage all tasks, and assign tasks. |
| `manager` | Can read users, create projects, modify projects they own, manage tasks in projects they own, and assign tasks. |
| `member` | Can read projects, create tasks, read assigned tasks, and update assigned tasks. Members cannot delete tasks or projects. |

Examples:

```text
Admin deletes any project: allowed
Manager updates own project: allowed
Manager updates another user's project: forbidden
Member updates assigned task: allowed
Member deletes a project: forbidden
```

Auth failures return `401 Unauthorized`. Permission failures return `403 Forbidden`.

## Task Query Parameters

Filtering:

```http
GET /tasks/?status=pending
GET /tasks/?priority=3
GET /tasks/?search=api
```

Pagination:

```http
GET /tasks/?skip=0&limit=10
```

Sorting:

```http
GET /tasks/?sort_by=due_date&order=asc
GET /tasks/?sort_by=priority&order=desc
```

Parameters can be combined:

```http
GET /tasks/?status=pending&priority=3&search=api&sort_by=due_date&order=asc&skip=0&limit=10
```

## Example Requests

Create a user:

```json
{
  "name": "Amina Bello",
  "email": "amina@example.com",
  "password": "Password1"
}
```

Create a project:

```json
{
  "name": "Customer Portal API",
  "description": "Backend API for customer profile and task tracking."
}
```

Create a task:

```json
{
  "title": "Build project endpoint",
  "description": "Create the project detail endpoint with nested tasks.",
  "priority": 4,
  "status": "pending",
  "due_date": "2026-08-30",
  "project_id": 1
}
```

## Validation and Error Handling

- Unknown request fields are rejected for create/update schemas.
- Duplicate user emails return `409 Conflict`.
- Missing users, projects, or tasks return `404 Not Found`.
- Invalid request bodies return `422 Unprocessable Entity`.
- Missing or invalid access tokens return `401 Unauthorized`.
- Authenticated users without permission return `403 Forbidden`.
- Too many auth requests return `429 Too Many Requests`.
- Database constraint problems return clear API errors where handled.

Common status codes:

```text
200 OK
201 Created
204 No Content
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
429 Too Many Requests
422 Unprocessable Entity
```

## Development Notes

Run migrations after model changes:

```powershell
.\venv\Scripts\python.exe -m alembic revision --autogenerate -m "describe change"
.\venv\Scripts\python.exe -m alembic upgrade head
```

Check current migration:

```powershell
.\venv\Scripts\python.exe -m alembic current
```

Run seed data:

```powershell
.\venv\Scripts\python.exe -m app.seed
```

Run server:

```powershell
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

## Testing

The API was tested through FastAPI's interactive docs at:

```text
http://127.0.0.1:8000/docs
```

Screenshots from endpoint testing are stored in the `assets/` folder.

## A few sample Screenshots

### User Endpoints

![Register user](assets/user_endpoints/users-register.png)

![List users](assets/user_endpoints/get-users.png)

### Project Endpoints

![Create project](assets/project_endpoints/post-project.png)

![Get project by ID](assets/project_endpoints/get_project_by_id.png)

### Task Endpoints

![Create task](assets/task_endpoints/post_task_success.png)


### Error Cases

![Duplicate email error](assets/test_error_cases/post_user_existing_email.png)
