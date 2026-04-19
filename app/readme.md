# Task API (FastAPI)

## 📌 Overview

A modular Task Management API built with FastAPI that supports full CRUD operations, filtering, and sorting.
This project demonstrates clean backend architecture using routers, schemas, and a service layer.

---

## 🚀 Features

* Create tasks with validation (title, priority, status, due date)
* Retrieve all tasks
* Retrieve a single task by ID
* Update tasks
* Delete tasks
* Filter tasks by:

  * status
  * priority
  * keyword search (title/description)
* Sort tasks by:

  * id, title, priority, status, due_date
* Proper HTTP status codes (201, 204, 404)

---

## 🛠 Tech Stack

* Python
* FastAPI
* Pydantic

---

## 📂 Project Structure

app/
├── main.py
├── routers/
│   └── task_router.py
├── schemas/
│   └── task_schema.py
├── services/
│   └── task_service.py

---

## ▶️ How to Run

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/task-api.git
cd task-api

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate   (Windows)

### 3. Install dependencies

pip install fastapi uvicorn

### 4. Run the server

uvicorn app.main:app --reload

### 5. Open API docs

http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### Create Task

POST /tasks/

### Get All Tasks

GET /tasks/

### Get Task by ID

GET /tasks/{task_id}

### Update Task

PUT /tasks/{task_id}

### Delete Task

DELETE /tasks/{task_id}

---

## 🔍 Query Parameters

### Filtering

GET /tasks?status=pending
GET /tasks?priority=3
GET /tasks?search=study

### Sorting

GET /tasks?sort_by=due_date&order=asc
GET /tasks?sort_by=priority&order=desc

---

## 📊 Status Codes

* 200 OK → successful GET
* 201 Created → successful POST
* 204 No Content → successful DELETE
* 404 Not Found → resource not found

---

## 💡 Notes

* Data is stored in-memory (no database yet)
* Designed for learning and demonstration purposes
