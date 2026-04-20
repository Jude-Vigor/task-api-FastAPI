# Task API (FastAPI)

## Overview

A modular Task Management API built with FastAPI that supports full CRUD operations, filtering, sorting, schema validation, and centralized error handling.

This project demonstrates clean backend architecture using routers, schemas, services, and custom exception handling.

---

## Features

* Create tasks with validation
* Retrieve all tasks
* Retrieve a single task by ID
* Update tasks
* Delete tasks
* Filter tasks by:

  * status
  * priority
  * keyword search
* Sort tasks by:

  * id
  * title
  * priority
  * status
  * due_date
  * created_at
* Automatic validation using Pydantic
* Custom centralized error handling using `@app.exception_handler`
* Response model includes `created_at`
* User input schema includes:

  * `email` with `EmailStr`
  * `password` with minimum 8 characters

---

## Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

---

## Project Structure

```text
app/
├── main.py
├── exceptions.py
├── routers/
│   └── task_router.py
├── schemas/
│   ├── task_schema.py
│   └── user_schema.py
├── services/
│   └── task_service.py
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/task-api.git
cd task-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install requirements.txt
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

### 5. Open the interactive docs

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Create Task

```http
POST /tasks/
```

### Get All Tasks

```http
GET /tasks/
```

### Get Task by ID

```http
GET /tasks/{task_id}
```

### Update Task

```http
PUT /tasks/{task_id}
```

### Delete Task

```http
DELETE /tasks/{task_id}
```

---

## Query Parameters

### Filtering

```http
GET /tasks?status=pending
GET /tasks?priority=3
GET /tasks?search=study
```

### Sorting

```http
GET /tasks?sort_by=due_date&order=asc
GET /tasks?sort_by=priority&order=desc
GET /tasks?sort_by=created_at&order=desc
```

---

## Task Schema Highlights

### TaskCreate / TaskUpdate

* `title`: minimum 3 characters
* `description`: optional
* `priority`: integer between 1 and 5
* `status`: enum (`pending`, `in_progress`, `completed`)
* `due_date`: must be a future date

### TaskResponse

* `id`
* `title`
* `description`
* `priority`
* `status`
* `due_date`
* `created_at`

### UserCreate

* `email`: validated with `EmailStr`
* `password`: minimum 8 characters

---

## Centralized Error Handling

This project uses a custom exception class and a centralized exception handler.

Example:

* `TaskNotFoundException`
* handled globally with `@app.exception_handler(TaskNotFoundException)`

This keeps route logic cleaner and ensures consistent error responses.

Example error response:

```json
{
  "detail": "Task with id 999 not found"
}
```

---

## Status Codes

* `200 OK` → successful GET and PUT
* `201 Created` → successful POST
* `204 No Content` → successful DELETE
* `404 Not Found` → task not found
* `422 Unprocessable Entity` → validation error

---

## Notes

* Data is currently stored in-memory using a Python list
* This project is designed for learning FastAPI architecture and API design principles
* Since there is no database yet, data resets whenever the server restarts
* `UserCreate` is currently a schema-only requirement and is not yet connected to a user registration endpoint
