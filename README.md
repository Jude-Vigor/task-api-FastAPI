# Project Management API

A FastAPI backend for managing users, projects, and tasks with PostgreSQL persistence.

This project started as a task CRUD API and now uses async SQLAlchemy, Alembic migrations, and relational data modeling. It includes user registration, project CRUD, task assignment, relationship loading, filtering, pagination, and seed data for testing.

## Features

- User CRUD
  - Register users
  - List users
  - Get user by ID
  - Get a user's projects
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

## Project Structure

```text
app/
|-- main.py
|-- database.py
|-- models.py
|-- exceptions.py
|-- seed.py
|-- routers/
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
'''

## Database Model


users
|-- id
|-- name
|-- email
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
```

Replace `postgres`, `YOUR_PASSWORD`, host, port, or database name with your local PostgreSQL settings.
Set `DB_ECHO=true` only when you want SQLAlchemy to print SQL queries while debugging.

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

### 8. Run the server

```powershell
.\venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

Open the interactive API docs:

```text
http://127.0.0.1:8000/docs
```

## API Endpoints

### Users

```http
POST /users/register
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
  "email": "amina@example.com"
}
```

Create a project:

```json
{
  "name": "Customer Portal API",
  "description": "Backend API for customer profile and task tracking.",
  "owner_id": 1
}
```

Create a task:

```json
{
  "title": "Build project endpoint",
  "description": "Create the project detail endpoint with nested tasks.",
  "priority": 4,
  "status": "pending",
  "due_date": "2026-05-30",
  "owner_id": 1,
  "project_id": 1
}
```

## Validation and Error Handling

- Unknown request fields are rejected for create/update schemas.
- Duplicate user emails return `409 Conflict`.
- Missing users, projects, or tasks return `404 Not Found`.
- Invalid request bodies return `422 Unprocessable Entity`.
- Database constraint problems return clear API errors where handled.

Common status codes:

```text
200 OK
201 Created
204 No Content
404 Not Found
409 Conflict
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

![Assign task](assets/task_endpoints/patch_task_id_assignee.png)

### Error Cases

![Duplicate email error](assets/test_error_cases/post_user_existing_email.png)

![Task project error](assets/test_error_cases/post_task_error.png)