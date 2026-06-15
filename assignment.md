


THE PIVOT BLUEPRINT

Builder Path — Backend Workbook

Python  |  FastAPI  |  PostgreSQL  |  Redis  |  Docker

Phase 2: The Architecture  |  Days 8–60
From Python refresher to 4 deployed APIs — including one with AI integration.

52 days. 1 hour per day. Job-ready.


Created by Racheal Kuranchie

Senior Software Engineer | Google Cloud Gen AI Leader

Cohort 1 | April 2026

How to Use This Workbook

Who This Is For
You know some Python. Maybe you’ve built basic scripts, done some Flask, or worked through OOP tutorials. But you haven’t built a production backend from scratch — with auth, databases, testing, Docker, and deployment. This workbook makes you job-ready in 52 days.


Why FastAPI?
FastAPI is the fastest-growing Python web framework. It’s async-native, has automatic API documentation, uses Pydantic for type-safe validation, and supports dependency injection. Companies hiring Python backend developers increasingly list FastAPI. It’s also genuinely fun to use.


What You’ll Build
4 complete, deployed APIs: a Task Manager, a Blog, a URL Shortener, and an AI-powered capstone project. Each one adds new skills: databases, auth, file uploads, email, caching, testing, Docker, and AI integration. By Day 60, you’ll have a portfolio that proves you can build production backend systems.


The 5 Rules

Rule 1: The 1-Hour Rule
One focused hour per day. Consistency compounds. Not 5 hours on Saturday.


Rule 2: Read the Articles
Videos give syntax. Articles give understanding. Every article in this workbook is a clickable link — read them.


Rule 3: Checkmarks, Not Commas
Every Build section is a checklist. Work through each item. Check it off. Feel the progress.


Rule 4: The AI Advantage
Every day has a specific AI prompt. Use Claude, ChatGPT, or Gemini as your thinking partner — not a copy-paste machine.


Rule 5: Rest Days Are Required
Your brain consolidates architectural patterns during rest. Skip rest and you plateau.


Your 8-Week Journey

Week
Theme
What You’ll Ship
Week 1
Python Refresher + FastAPI Foundations
Task Management API (Python refresher + FastAPI)
Week 2
SQL Foundations + Database Integration
Database-backed API (SQL + SQLAlchemy + migrations)
Week 3
Authentication & Authorization
Secure API (JWT, refresh tokens, RBAC)
Week 4
File Uploads, Email, Caching & Background Jobs
Blog API + URL Shortener (files, email, cache)
Week 5
Testing & Professional Code Quality
Tested APIs with CI/CD + URL Shortener
Week 6
Docker, Deployment & Production
Docker + 3 APIs deployed to the cloud
Week 7
Capstone: AI-Powered Backend
AI-Powered Capstone (Claude/OpenAI integration)
Week 8
Phase 2 Wrap-Up — Ship, Reflect, Prepare
Portfolio polished, story published, job-ready


By Day 60, You Will Have:
4 deployed APIs on the internet with live documentation. An AI-powered capstone that makes hiring managers stop scrolling. Automated tests, CI/CD pipelines, Docker containers, and cloud deployments. A GitHub profile that screams “this person builds production backend systems.” A published technical article and updated LinkedIn presence. The skills and proof to get hired as a backend developer.



Week 1: Python Refresher + FastAPI Foundations

Days 8–14  |  Phase 2: The Architecture

This Week’s Theme
Days 8–10 rebuild your Python muscle memory. Days 11–13 introduce FastAPI — the modern Python web framework that’s taking over the backend world. By the end of this week, you have a working API.


DAY 8  |  Python Refresher — Data Types, Functions & Control Flow
Objective
Shake off the rust — confirm you can write clean Python confidently
🎥 Watch
“Python in 100 Seconds” by Fireship  •  “Python for Beginners” by Mosh (first 30 min for refresher)
📚 Read
Python Cheat Sheet — quick reference for all Python fundamentals
Python Coding Style (PEP 8) — the style guide every Python developer follows
🛠️ Build
Create a new folder: backend-learning/ with a virtual environment (python -m venv venv)
Write 5 functions: calculate_age(birth_year), format_currency(amount), celsius_to_fahrenheit(temp), is_palindrome(text), count_vowels(text)
Practice with lists, dicts, tuples, and sets — write a function that takes a list of dicts and returns the one with the highest value for a given key
Use list comprehensions: filter even numbers, create a dict from two lists, flatten a nested list
Practice string methods: split, join, strip, replace, f-strings with formatting
Write a function that reads a CSV file and returns a list of dictionaries (one per row)
Handle errors: wrap file reading in try/except and return a helpful error message
🤖 AI Prompt
"I’m refreshing my Python. Test me: give me 5 increasingly difficult coding challenges that cover data types, functions, list comprehensions, dictionary manipulation, and file handling. Don’t give me the solutions yet — let me try first."



DAY 9  |  Python OOP — Classes, Inheritance & Data Models
Objective
Understand object-oriented Python — FastAPI’s Pydantic models build on this
🎥 Watch
“Python OOP Tutorial” by Corey Schafer (first 30 min)
📚 Read
Classes and Objects — official Python class tutorial
Dataclasses Guide — modern Python data classes (foundation for Pydantic)
🛠️ Build
Create a User class with: name, email, role attributes and a greet() method
Create a Task class with: title, description, status, priority, due_date, and a is_overdue() method
Create a Project class that contains a list of Tasks and methods: add_task(), remove_task(), get_tasks_by_status()
Use inheritance: create an AdminUser that extends User with extra permissions
Convert your Task class to a dataclass (from dataclasses import dataclass)
Add type hints to ALL your code: def add_task(self, task: Task) -> None
Write a __repr__ method for each class so printing objects shows useful info
🤖 AI Prompt
"Explain Python dataclasses and why they’re the foundation for Pydantic models. Show me the same data model as a regular class, then a dataclass, then a Pydantic BaseModel. What does each version give me for free?"



DAY 10  |  Python Advanced Patterns — Decorators, Context Managers & Error Handling
Objective
Master the patterns that make Python code professional and production-ready
🎥 Watch
“Python Decorators in 15 Minutes” by Socratica  •  “Context Managers” by Corey Schafer (12 min)
📚 Read
Decorators Guide — complete decorators tutorial
Exception Handling — official error handling guide
🛠️ Build
Write a @timer decorator that logs how long a function takes to execute
Write a @retry(max_attempts=3) decorator that retries a function on failure
Create custom exception classes: ValidationError, NotFoundError, AuthenticationError
Write a function that raises your custom exceptions with helpful messages
Use a context manager to safely handle file operations (with open() as f)
Write a context manager class that handles database-like connections (enter/exit)
Practice: async/await basics — write an async function that simulates a slow API call
🤖 AI Prompt
"Explain Python decorators like I’m wrapping a gift. The function is the gift, the decorator is the wrapping paper. Walk me through: a simple decorator, a decorator with arguments, and a decorator that preserves the original function’s metadata (functools.wraps)."



DAY 11  |  FastAPI — Your First API in 15 Minutes
Objective
Set up FastAPI and build your first endpoints — see why it’s the fastest-growing Python framework
🎥 Watch
“FastAPI Course for Beginners” by freeCodeCamp (first 30 min)  •  “FastAPI in 5 Minutes” by Fireship
📚 Read
FastAPI Tutorial — First Steps — official getting started guide
Path Parameters — dynamic URL parameters
Query Parameters — filtering and pagination params
🛠️ Build
Install: pip install fastapi uvicorn python-dotenv
Create app/main.py with a FastAPI() instance and a root endpoint that returns {"message": "Hello World"}
Run with: uvicorn app.main:app --reload
Visit /docs — explore the auto-generated Swagger UI (this is FastAPI’s superpower)
Create 3 GET endpoints: /health, /items, /items/{item_id}
Add query parameters: /items?category=electronics&min_price=10
Create a POST endpoint that accepts JSON body and returns the created object
Test every endpoint in the /docs Swagger UI — click “Try it out”
🤖 AI Prompt
"I just built my first FastAPI endpoint. Explain what makes FastAPI different from Flask: auto-generated docs, async support, Pydantic validation, dependency injection, and type hints. For each advantage, show me a concrete example."



DAY 12  |  Pydantic Models — Validation That Writes Itself
Objective
Use Pydantic for automatic request/response validation — FastAPI’s killer feature
🎥 Watch
“Pydantic V2 Tutorial” by ArjanCodes (20 min)
📚 Read
Request Body — using Pydantic models for request validation
Response Model — controlling what your API returns
Pydantic Field Validators — custom validation rules
🛠️ Build
Create a TaskCreate schema: title (min 3 chars), description (optional), priority (1-5), status (enum: pending/in_progress/done), due_date (must be future date)
Create a TaskResponse schema that includes id and created_at
Create a UserCreate schema with email validation (use EmailStr) and password (min 8 chars)
Use response_model on your endpoints to control what data is returned
Add custom validators: @field_validator for business rules (e.g., due_date must be in the future)
Test validation by sending invalid data via /docs — see the automatic 422 error responses
Create a centralized error handler using @app.exception_handler for custom exceptions
🤖 AI Prompt
"Show me the same validation in Flask (manual if/else checks) vs FastAPI (Pydantic). Compare: lines of code, error messages returned, what happens when I forget a field. Why does Pydantic make APIs more reliable?"



DAY 13  |  BUILD DAY: Task Management API v1
Objective
Ship a complete CRUD API with validation, error handling, and auto-generated documentation
🎥 Watch
“REST API Design Best Practices” by Traversy Media (15 min)
📚 Read
REST Naming Conventions — the rules senior devs follow
HTTP Status Codes — reference for every status code
🛠️ Build
Organize your project: app/ with main.py, routers/, schemas/, services/
Create a task router using APIRouter with proper tags
Implement full CRUD: create task, list all tasks, get by ID, update task, delete task
Add a service layer: routers call services, services handle business logic
Add filtering: GET /tasks?status=pending&priority=3&search=keyword
Add sorting: GET /tasks?sort_by=due_date&order=desc
Return proper HTTP status codes: 201 for create, 204 for delete, 404 for not found
Visit /docs and verify every endpoint is documented and testable
Write a README with: project overview, how to run, and API endpoint list
Push to GitHub with a clean .gitignore
🤖 AI Prompt
"Review my FastAPI Task API. Evaluate: REST compliance, Pydantic usage, error handling consistency, code organization (is my service layer clean?), and naming conventions. What would a senior backend developer change? [paste your router + service files]"



DAY 14  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 1 Reflection:
You rebuilt your Python in 3 days and built a professional API in 3 more. Open /docs and click through every endpoint. That auto-generated documentation is something Flask developers have to build manually. What part of FastAPI surprised you the most?



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Write clean Python with type hints, list comprehensions, and error handling
Create classes and dataclasses with proper methods and inheritance
Set up FastAPI with routes, query params, and path params
Use Pydantic schemas for automatic request/response validation
Build a complete CRUD API with proper status codes and error handling



Week 2: SQL Foundations + Database Integration

Days 15–21  |  Phase 2: The Architecture

This Week’s Theme
Your API stores data in memory — restart the server and everything vanishes. This week you learn SQL from the ground up, then connect your API to a real PostgreSQL database.


DAY 15  |  SQL Fundamentals — SELECT, WHERE, JOINs
Objective
Learn to query databases — the language every backend developer speaks daily
🎥 Watch
“SQL Tutorial for Beginners” by Programming with Mosh (first 40 min)  •  “SQL in 100 Seconds” by Fireship
📚 Read
SQLBolt Interactive Tutorial — lessons 1–8 with hands-on exercises (DO these)
Visual SQL Joins — the classic visual explanation of JOIN types
🛠️ Build
Use SQLBolt (sqlbolt.com) or DB Fiddle (db-fiddle.com) — no installation needed
Write 5 SELECT queries: all rows, specific columns, with WHERE filter, with ORDER BY, with LIMIT
Write queries with conditions: AND/OR, BETWEEN dates, LIKE for partial text match, IN for multiple values
Practice JOINs: INNER JOIN two tables, LEFT JOIN to find missing relationships
Write a query that joins 3 tables (e.g., users → orders → products)
Use aliases to keep queries readable: SELECT u.name, o.total FROM users u JOIN orders o ON u.id = o.user_id
Handle NULLs: find rows where a column IS NULL, use COALESCE for defaults
Save all your queries in a sql-practice.sql file with comments explaining each one
🤖 AI Prompt
"I’m learning SQL from scratch. Explain SELECT, FROM, WHERE, JOIN, and ORDER BY using a school analogy: tables are classrooms, rows are students, columns are attributes. Walk me through 5 queries with increasing complexity."



DAY 16  |  SQL Power Tools — GROUP BY, Aggregations & Subqueries
Objective
Summarize data, count things, and write queries that answer real business questions
🎥 Watch
“SQL GROUP BY and Aggregates” by Socratica (15 min)  •  “Subqueries in SQL” by Socratica (12 min)
📚 Read
SQLBolt Lessons 10–13 — aggregates and grouping (complete these exercises)
CTEs Explained — Common Table Expressions — clean complex queries
🛠️ Build
Write aggregate queries: COUNT, SUM, AVG, MIN, MAX on a dataset
Use GROUP BY: count orders per customer, total revenue per product category
Use HAVING: find customers with more than 5 orders, categories with revenue above $10,000
Write a subquery: find all customers whose total spend is above the average
Write a CTE that calculates monthly revenue, then finds the highest-revenue month
Create a table: write CREATE TABLE with proper column types, PRIMARY KEY, NOT NULL, UNIQUE constraints
Write INSERT, UPDATE, DELETE statements and understand how foreign keys protect data integrity
Design a schema for your Task API: users table, projects table, tasks table with proper foreign keys
🤖 AI Prompt
"Explain the difference between WHERE and HAVING like I’m filtering job applicants. WHERE filters individual applicants (before grouping), HAVING filters the summary stats (after grouping). Give me 3 real scenarios where I need HAVING."



DAY 17  |  SQLAlchemy — Connecting Python to PostgreSQL
Objective
Define database models in Python and let the ORM handle the SQL
🎥 Watch
“SQLAlchemy 2.0 Tutorial” by ArjanCodes (25 min)
📚 Read
SQLAlchemy 2.0 Quickstart — official ORM quickstart
FastAPI + SQLAlchemy Guide — official FastAPI database integration
🛠️ Build
Install PostgreSQL locally or use a free cloud database (ElephantSQL or Supabase)
Install: pip install sqlalchemy asyncpg alembic psycopg2-binary
Create app/database.py: async engine, async session factory, Base model class
Create a database dependency: async def get_db() that yields an AsyncSession
Define a User model: id (primary key), name, email (unique), password_hash, role, created_at
Define a Task model: id, title, description, status, priority, due_date, owner_id (foreign key to users), created_at
Set up Alembic: alembic init alembic, configure alembic.ini with your DATABASE_URL
Create and run your first migration: alembic revision --autogenerate -m "create users and tasks", alembic upgrade head
Verify tables exist in your database using a SQL client or psql command
🤖 AI Prompt
"I’m setting up async SQLAlchemy with FastAPI. Walk me through: creating the async engine, the session dependency with Depends(), and why async matters for a web API. Show me common mistakes with async sessions (like forgetting to await)."



DAY 18  |  Relationships & Queries in SQLAlchemy
Objective
Model relationships between tables and write queries that fetch related data efficiently
🎥 Watch
“SQL Joins Explained” by Web Dev Simplified (12 min)
📚 Read
SQLAlchemy Relationships — one-to-many, many-to-many relationship guide
Eager Loading Strategies — avoid N+1 queries with selectinload
🛠️ Build
Add a Project model: id, name, description, owner_id (FK to users), created_at
Define relationships: User has many Projects, Project has many Tasks, Task belongs to a User (assignee)
Add a many-to-many: Tasks can have multiple Tags (create a tags table and association table)
Create an Alembic migration for the new models: alembic revision --autogenerate
Write queries: get all tasks for a user (with eager loading), get a project with all its tasks and assignees
Use selectinload() to avoid the N+1 query problem
Create a seed script (seed.py) that populates the database with 5 users, 3 projects, 20 tasks, and 10 tags
Run the seed script and verify data with SQL queries
🤖 AI Prompt
"Explain the N+1 query problem like I’m ordering food for 10 friends. Without eager loading, I make 1 query for the table, then 10 separate queries for each person’s order. Show me the problem and the fix using SQLAlchemy’s selectinload()."



DAY 19  |  Rewriting the API to Use the Database
Objective
Replace in-memory storage with real database operations — your API becomes permanent
🎥 Watch
“FastAPI with Database” by Pretty Printed (20 min)
📚 Read
FastAPI Depends() — dependency injection — the pattern that makes FastAPI special
Alembic Tutorial — migration management for production
🛠️ Build
Rewrite your task service to use async SQLAlchemy sessions instead of in-memory lists
Use Depends(get_db) in every route to get a database session
Implement: create_task (INSERT), get_tasks (SELECT with filters), get_task_by_id, update_task, delete_task
Add pagination: skip and limit query parameters with proper SQL OFFSET/LIMIT
Add filtering: by status, priority, and search text (ILIKE for case-insensitive search)
Handle database errors: IntegrityError (duplicate email), NoResultFound (task not found)
Test every endpoint in /docs with real data — restart the server and verify data persists
🤖 AI Prompt
"My API was using in-memory lists and now I’m switching to SQLAlchemy. Show me the before/after for a create_task service function. What changes? What stays the same? How do I handle the async session lifecycle correctly?"



DAY 20  |  BUILD DAY: Database-Backed Project Management API
Objective
Your API is now backed by PostgreSQL with proper data modeling and migrations
🎥 Watch


📚 Read
SQLAlchemy Error Handling — handling database errors in production
🛠️ Build
Verify all CRUD endpoints work with the database
Add user CRUD endpoints: register (no auth yet), list users, get user by ID
Add project CRUD endpoints: create, list (with task count), get with tasks, update, delete
Add task assignment: PATCH /tasks/{id}/assign with assignee_id in body
Ensure all relationships work: get a user’s projects, get a project’s tasks with assignees
Seed the database with realistic data and test all queries
Update your README with database setup instructions (how to install Postgres, run migrations, seed)
Push to GitHub with a clean commit history
🤖 AI Prompt
"My API uses PostgreSQL with SQLAlchemy. I want to add a feature: when I delete a project, all its tasks should also be deleted. Should I use CASCADE in the database, handle it in Python code, or both? Explain the tradeoffs and show me the SQLAlchemy configuration."



DAY 21  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 2 Reflection:
You learned SQL from scratch and connected your API to a real database in one week. Restart your server — your data is still there. That’s the difference between a toy and a real application. Which SQL concept was the biggest ‘aha’ moment?






WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Write SQL queries with JOINs, GROUP BY, and aggregations
Define SQLAlchemy models with relationships and type hints
Run Alembic migrations to manage schema changes
Use async sessions with FastAPI’s dependency injection
Handle database errors gracefully and return user-friendly messages



Week 3: Authentication & Authorization

Days 22–28  |  Phase 2: The Architecture

This Week’s Theme
Your API is open to anyone right now. This week you lock it down: hashed passwords, JWT tokens, protected routes, and role-based access control.


DAY 22  |  Password Hashing & User Registration
Objective
Store passwords securely — never, ever in plain text
🎥 Watch
“Password Hashing Explained” by Computerphile (10 min)  •  “JWT Authentication” by Web Dev Simplified (15 min)
📚 Read
OWASP Password Storage — industry standard for password security
Why Hashing Matters — clear explanation of hashing vs encryption
🛠️ Build
Install: pip install passlib[bcrypt]
Create app/auth/security.py with hash_password() and verify_password() functions using CryptContext
Create a UserCreate Pydantic schema with: email (EmailStr), password (min 8 chars, must contain a number), name
Create a UserResponse schema that NEVER includes the password hash
Build POST /auth/register: validate input, hash password, save to database, return user without password
Add a unique constraint on email — handle duplicate registration attempts with a clear error
Register 3 test users and verify passwords are hashed in the database (not plain text)
🤖 AI Prompt
"Explain bcrypt like I’m locking a house. What are salt rounds? Why is bcrypt better than SHA-256 for passwords? What happens if I use 4 rounds vs 12 rounds? Show me the security vs performance tradeoff with real numbers."



DAY 23  |  JWT Tokens & Login
Objective
Issue tokens that prove identity without storing sessions on the server
🎥 Watch
“JWT Explained in 5 Minutes” by Fireship
📚 Read
JWT Introduction — interactive JWT debugger — paste a token and see what’s inside
FastAPI OAuth2 with JWT — official FastAPI JWT tutorial
🛠️ Build
Install: pip install python-jose[cryptography]
Create functions: create_access_token(data, expires_delta) and verify_token(token)
Set up OAuth2PasswordBearer(tokenUrl="auth/login") — this auto-adds the Authorize button in /docs
Build POST /auth/login: accept email + password, verify credentials, return JWT token
Include user_id and role in the token payload with a 24-hour expiration
Build GET /auth/me: decode the token and return the current user’s profile
Test the full flow in /docs: register → login → copy token → click Authorize → access /auth/me
🤖 AI Prompt
"Walk me through the complete JWT flow step by step: user logs in → server creates token → client stores it → client sends it with every request → server verifies it. What happens at each step? What are the security risks at each point?"





DAY 24  |  Auth Dependencies & Protected Routes
Objective
Protect endpoints so only authenticated users can access them
🎥 Watch
“FastAPI Dependencies” by Pretty Printed (15 min)
📚 Read
FastAPI Security Tutorial — comprehensive security guide (read all sections)
Dependency Injection — the pattern that makes auth clean in FastAPI
🛠️ Build
Create get_current_user dependency: extract token from header, decode it, query database for user
Handle all edge cases: missing token (401), expired token (401), tampered token (401), deleted user (401)
Apply Depends(get_current_user) to all task and project endpoints
Keep /auth/register and /auth/login public (no auth required)
Modify task creation: automatically set owner_id from the authenticated user (not from request body)
Modify task listing: users only see their own tasks (filter by owner_id)
Test: access a protected route without token (should get 401), with valid token (should work)
Verify /docs shows lock icons on protected endpoints
🤖 AI Prompt
"Show me how FastAPI’s Depends() pattern makes auth clean. Compare: auth in Flask (decorators, g.user) vs FastAPI (dependency injection, type hints). Which is more testable? Why can I override dependencies in tests?"



DAY 25  |  Role-Based Access Control (RBAC)
Objective
Different users should have different permissions — admins, managers, and members
🎥 Watch
“Role Based Access Control Explained” by IBM Technology (8 min)
📚 Read
RBAC Concepts — industry-standard RBAC explanation
FastAPI Handling Errors — custom exception handlers
🛠️ Build
Add a role field to your User model: admin, manager, member (use a Python Enum)
Create a require_role dependency: checks if current user has the required role, returns 403 if not
Stack dependencies: Depends(require_role("admin", "manager")) on specific routes
Implement rules: admins can delete any project, managers can only modify their own, members can only update assigned tasks
Create a permissions matrix and test EVERY combination (3 roles × all CRUD operations)
Ensure error messages are generic: don’t reveal “user not found” vs “wrong password” (always “Invalid credentials”)
🤖 AI Prompt
"I have 3 roles: admin, manager, member. Help me build a permissions matrix showing exactly what each role can do for Users, Projects, and Tasks. Then show me the FastAPI dependency that enforces this cleanly."





DAY 26  |  Refresh Tokens & Security Hardening
Objective
Handle token expiration gracefully and protect against common attacks
🎥 Watch
“Refresh Token Rotation” by Auth0 (10 min)
📚 Read
JWT Best Practices — production JWT patterns
OWASP API Security Top 10 — the threats your API faces
🛠️ Build
Implement refresh tokens: short-lived access token (15 min) + long-lived refresh token (7 days)
Store refresh tokens in the database with user_id, token hash, and expiration
Build POST /auth/refresh: accept refresh token, verify it, issue new access + refresh token pair
Invalidate old refresh tokens on rotation (delete from database)
Add rate limiting on /auth endpoints: pip install slowapi (5 requests per minute)
Configure CORS properly: only allow your frontend origin, not *
Run through the OWASP API Security Top 10 — check which ones your API handles
🤖 AI Prompt
"I’m implementing refresh tokens. Walk me through the FULL flow: login → get access + refresh → access expires → use refresh to get new pair → refresh rotation. What attacks does each step prevent? What happens if someone steals a refresh token?"



DAY 27  |  BUILD DAY: Secure Project Management API
Objective
Your API now has production-grade auth that protects real data
🎥 Watch


📚 Read
JWT Security Testing — test your JWT implementation for vulnerabilities
🛠️ Build
Test the complete auth flow: register → login → access protected routes → refresh token → logout
Test RBAC with 3 different user accounts (one per role)
Test security: try accessing resources you shouldn’t (member trying to delete a project)
Test edge cases: expired tokens, tampered tokens, deleted users, rate limiting
Update /docs: all protected endpoints should show the lock icon and require authorization
Update README with auth documentation: how to register, login, use tokens, role permissions
Create a Postman collection with auth tests and export it to your repo
Push clean code to GitHub
🤖 AI Prompt
"Act as a penetration tester. Here’s my auth implementation: [describe endpoints and flow]. What are the top 5 attacks you’d try? For each, show me the attack and whether my current setup prevents it."



DAY 28  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 3 Reflection:
You built the same auth system that protects real production APIs: hashed passwords, JWT, refresh tokens, RBAC. Most bootcamp graduates have never built this from scratch. Log into /docs with your admin account and feel that lock icon — you built that security.



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Hash passwords with bcrypt and never store or return plain text
Issue and verify JWT tokens with proper expiration
Protect routes using FastAPI’s dependency injection pattern
Implement role-based access control for 3 roles
Handle refresh token rotation and rate limiting



Week 4: File Uploads, Email, Caching & Background Jobs

Days 29–35  |  Phase 2: The Architecture

This Week’s Theme
Real APIs don’t just CRUD data. They send emails, upload files, cache responses, and run background jobs. This week your API grows into a real system.


DAY 29  |  File Uploads & Cloud Storage
Objective
Accept file uploads and store them in the cloud — never on your application server
🎥 Watch
“FastAPI File Upload” by Pretty Printed (15 min)
📚 Read
FastAPI File Handling — official file upload guide
Supabase Storage — free cloud storage (S3 alternative)
🛠️ Build
Create POST /users/me/avatar: accept an image upload using FastAPI’s UploadFile
Validate: only allow jpg/png (check content_type), max 5MB (check file size)
Upload to Supabase Storage or Cloudinary (both have free tiers)
Store the returned URL in the user’s avatar_url database field
Return the URL in user responses
Add project attachment uploads: POST /projects/{id}/attachments
Handle errors: file too large, invalid type, storage service unavailable
🤖 AI Prompt
"I’m implementing file uploads in FastAPI. What are the security risks? Walk me through: why I shouldn’t trust file.content_type blindly, why I should validate file signatures (magic bytes), and why files should NEVER be stored in my application folder."



DAY 30  |  Email Sending & Password Reset
Objective
Send transactional emails and implement a secure password reset flow
🎥 Watch
“Sending Emails with Python” by Tech with Tim (12 min)
📚 Read
Resend Python SDK — modern email API (free tier)
FastAPI Background Tasks — run tasks without blocking the response
🛠️ Build
Sign up for Resend (free tier) and get an API key
Create an email service: send_email(to, subject, html_body) using Resend’s Python SDK
Send a welcome email when a user registers (use FastAPI’s BackgroundTasks so registration doesn’t wait for email)
Implement password reset: POST /auth/forgot-password generates a time-limited token, sends email with reset link
Implement POST /auth/reset-password: verify token, update password, invalidate the token
Create HTML email templates using Jinja2 (professional-looking, not plain text)
Handle email failures gracefully: never let a failed email break a user action
🤖 AI Prompt
"I’m implementing password reset. Walk me through the SECURE flow: user requests reset → generate a random token with expiration → hash the token and store in database → send unhashed token in email link → user clicks link → verify by hashing submitted token and comparing. Why hash the reset token?"



DAY 31  |  Redis Caching & Background Jobs
Objective
Make your API faster with caching and handle slow operations in the background
🎥 Watch
“Caching Explained” by Fireship (5 min)  •  “Redis Crash Course” by Traversy Media (first 15 min)
📚 Read
Redis Getting Started — Redis quickstart
Caching Best Practices — when and how to cache (cache-aside pattern)
🛠️ Build
Install Redis locally (or use a free cloud Redis like Upstash) and pip install redis
Create a caching service with: cache_set(key, data, ttl), cache_get(key), cache_delete(key)
Cache the task list endpoint: check Redis first, if miss then query database and cache the result
Invalidate cache when tasks are created, updated, or deleted
Measure response times before and after caching (print the time difference)
Move email sending to a proper background job using FastAPI’s BackgroundTasks
Create a background job for a “generate report” endpoint: return 202 Accepted immediately, process in background
🤖 AI Prompt
"I cached my task list but users see stale data after creating a task. Explain 3 cache invalidation strategies: time-based (TTL), event-based (delete on write), and tag-based (group related caches). Which should I use for a CRUD API and why?"



DAY 32  |  API Documentation & Configuration
Objective
Make your auto-generated docs production-ready and your config type-safe
🎥 Watch
“OpenAPI Specification” by APIs You Won’t Hate (12 min)
📚 Read
FastAPI Metadata — customizing your auto-generated docs
Pydantic Settings — type-safe environment configuration
🛠️ Build
Install: pip install pydantic-settings
Create app/config.py with a Settings(BaseSettings) class: DATABASE_URL, JWT_SECRET, REDIS_URL, RESEND_API_KEY, all typed
Add .env file with all values and .env.example with placeholders
Configure FastAPI metadata: title, description, version, contact info
Add tags to every router for organized endpoint grouping in /docs
Add response_model_exclude_none=True to hide optional null fields
Add example values to your Pydantic schemas so /docs shows realistic request bodies
Visit /docs and /redoc — both should look professional and be fully interactive
🤖 AI Prompt
"FastAPI’s pydantic-settings validates env vars at startup. Show me a Settings class for my API with: required strings (DATABASE_URL, JWT_SECRET), optional with defaults (DEBUG=False, LOG_LEVEL="info"), and a list (ALLOWED_ORIGINS). What happens if I forget to set DATABASE_URL?"



DAY 33  |  Mini Project: Blog API with Full Features
Objective
Build a second API from scratch that uses everything you’ve learned — solidify the patterns
🎥 Watch


📚 Read
REST API Design Guide — comprehensive API design reference
🛠️ Build
Build a Blog API with: users (auth), posts (CRUD + publish/draft status), comments (nested under posts), tags (many-to-many with posts)
Auth: register, login, JWT, only post authors can edit/delete their posts
Posts: create (draft), update, publish, list (paginated, filterable by tag/author/status), get single with comments
Comments: create (authenticated), list for a post, delete (only author or post owner)
Add: featured image upload on posts, email notification when someone comments on your post
Cache the published posts list (most frequently accessed endpoint)
Full Pydantic validation on every endpoint
Auto-generated docs should be comprehensive and testable
🤖 AI Prompt
"I’m building a Blog API and need to design the database schema. I have: users, posts (with draft/published status), comments, and tags (many-to-many). Review my ERD and suggest improvements for: data integrity, query performance, and future scalability."



DAY 34  |  BUILD DAY: Ship the Blog API
Objective
Complete, test, and document your second production-grade API
🎥 Watch


📚 Read
The Twelve-Factor App — how production applications should be built (read all 12)
🛠️ Build
Verify all endpoints work end-to-end: register → login → create draft → add tags → publish → comment → cache hit
Run through /docs and test every endpoint interactively
Handle all edge cases: commenting on a draft (should fail), deleting someone else’s post (403)
Write a comprehensive README: endpoints, auth flow, database setup, features
Push to GitHub as a separate repo from your Task API
You now have 2 production-grade APIs in your portfolio
🤖 AI Prompt
"Review my Blog API against the Twelve-Factor App methodology. Which factors am I following? Which am I violating? What’s the most critical thing to fix before deploying to production?"



DAY 35  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 4 Reflection:
You now have 2 complete APIs: a Task Manager and a Blog. Both have auth, databases, file uploads, email, caching, and auto-generated docs. You built the Blog API faster because the patterns are second nature now. That’s the sign of a real engineer.



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Upload files to cloud storage with validation
Send transactional emails with background tasks
Implement Redis caching with proper invalidation
Configure apps with type-safe pydantic-settings
Build a complete API from scratch using all learned patterns



Week 5: Testing & Professional Code Quality

Days 36–42  |  Phase 2: The Architecture

This Week’s Theme
Untested code is broken code you haven’t found yet. This week you learn to test like a professional and set up the automation that real teams use.


DAY 36  |  Unit Testing with pytest
Objective
Write your first tests and understand why testing matters for getting hired
🎥 Watch
“pytest Tutorial” by ArjanCodes (20 min)
📚 Read
pytest Getting Started — official quickstart
Test Pyramid — essential reading on testing strategy
🛠️ Build
Install: pip install pytest pytest-asyncio httpx
Create tests/ directory with conftest.py for shared fixtures
Write 5 unit tests for your service layer: test task creation, test validation (invalid priority), test filtering logic, test password hashing, test token creation
Use the AAA pattern: Arrange (set up data), Act (call the function), Assert (check the result)
Use pytest fixtures for reusable test data (test user, test task)
Run tests: pytest -v (see each test pass or fail with details)
Add pytest to your requirements.txt as a dev dependency
🤖 AI Prompt
"I’m writing my first tests. Show me the AAA pattern with 3 FastAPI examples: testing a Pydantic schema validation, testing a service function, and testing a utility function. How do I test async functions with pytest-asyncio?"



DAY 37  |  Integration Testing — Testing the Full API
Objective
Test your endpoints end-to-end through HTTP requests — as a real client would use them
🎥 Watch
“Unit vs Integration vs E2E Testing” by Fireship (6 min)
📚 Read
FastAPI Testing Docs — official testing guide with TestClient and dependency overrides
Testing FastAPI Apps — comprehensive testing guide
🛠️ Build
Create a test database (separate from development): use SQLite for testing or a test PostgreSQL db
Override the database dependency: app.dependency_overrides[get_db] = get_test_db
Write integration tests using httpx.AsyncClient: test the complete auth flow (register → login → access protected route)
Test CRUD through HTTP: create a task (201), get it (200), update it (200), delete it (204), get again (404)
Test error cases: missing required field (422), duplicate email (409), non-existent ID (404), unauthorized (401)
Test RBAC: verify a member can’t delete a project (403)
Aim for 20+ integration tests covering all critical paths
🤖 AI Prompt
"FastAPI lets me override any dependency in tests. Show me how to: override the database with a test database, override the email service with a mock, and override auth to test as different user roles. This is FastAPI’s testing superpower."



DAY 38  |  Mocking, Fixtures & CI/CD
Objective
Isolate external services in tests and automate everything with GitHub Actions
🎥 Watch
“GitHub Actions Tutorial” by Fireship (10 min)
📚 Read
GitHub Actions Quickstart — CI/CD automation
GitHub Actions + PostgreSQL — database in CI
🛠️ Build
Mock external services: email (verify it was called without actually sending), file upload (return a fake URL)
Use FastAPI’s dependency_overrides to inject mocks cleanly
Create test factories: create_test_user(), create_test_task() that generate realistic test data
Create .github/workflows/test.yml: trigger on push, set up Python, install deps, start PostgreSQL, run migrations, run tests with coverage
Add --cov=app --cov-fail-under=70 to fail if coverage drops below 70%
Push and verify the workflow runs successfully on GitHub
Add a CI passing badge to your README
🤖 AI Prompt
"Help me write a complete GitHub Actions workflow for my FastAPI app: set up Python 3.12, start a PostgreSQL service container, install requirements, run Alembic migrations, run pytest with coverage, and fail if coverage is below 70%."



DAY 39  |  Logging & Error Tracking
Objective
Know what your API is doing in production before users report problems
🎥 Watch
“Sentry Error Tracking” by Fireship (6 min)
📚 Read
Python Logging — official logging guide
Sentry for FastAPI — error tracking setup
🛠️ Build
Set up structured logging with Python’s logging module (or install loguru for a cleaner API)
Create a FastAPI middleware that logs every request: method, path, status code, duration in ms
Log errors with full context: stack trace, request body, user ID
Use log levels appropriately: DEBUG for development, INFO for requests, WARNING for recoverable errors, ERROR for failures
Set up Sentry (free tier): pip install sentry-sdk[fastapi], add sentry_sdk.init() in main.py
Trigger a test error and verify it appears in your Sentry dashboard
Add a GET /health endpoint that returns API status, database connectivity, and Redis status
NEVER log passwords, tokens, or personal data
🤖 AI Prompt
"What should I log in a production API and what should I NEVER log? Give me a logging strategy covering: request logs, error logs, security events (failed logins), and performance warnings. What sensitive data must I always exclude?"



DAY 40  |  Mini Project: URL Shortener API
Objective
Build a third API rapidly to prove the patterns are second nature
🎥 Watch


📚 Read
FastAPI Best Practices — community-curated best practices
🛠️ Build
Build a URL Shortener API in one session (you have all the patterns):
POST /shorten: accept a long URL, generate a short code, return the short URL
GET /{code}: redirect to the original URL (HTTP 307 redirect)
GET /{code}/stats: return click count, creation date, last clicked date
Auth: optional — authenticated users can see their link history
Cache popular redirects in Redis (most links get clicked within the first hour)
Track analytics: increment click count, log referrer and user-agent
Add rate limiting: max 10 shortens per minute per IP
Write 10 tests, set up CI/CD, deploy (you’ll do deployment next week)
🤖 AI Prompt
"I’m building a URL shortener. How should I generate short codes? Compare: random string, base62 encoding of an auto-increment ID, and hashing. What are the collision risks of each? Which would you use for a production service?"



DAY 41  |  BUILD DAY: All APIs Tested & Monitored
Objective
Every API in your portfolio has tests, CI/CD, logging, and error tracking
🎥 Watch


📚 Read
Clean Code Python — Python clean code principles
🛠️ Build
Run full test suites on all 3 APIs: Task Manager, Blog, URL Shortener
All tests pass with 70%+ coverage
All 3 repos have GitHub Actions CI that runs on push
Sentry is connected and capturing errors on at least one API
Structured logging on all request handlers
Clean up ALL code: consistent naming, remove print statements, add docstrings to services
Push everything with conventional commit messages
🤖 AI Prompt
"My test coverage is at [X]%. Which parts of a FastAPI backend are MOST important to test? Rank: auth middleware, Pydantic validation, service business logic, database queries, error handling, utility functions. What can I skip and what is non-negotiable?"



DAY 42  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 5 Reflection:
You have 3 tested APIs with automated CI pipelines. When you push code, tests run automatically. When errors happen in production, Sentry tells you immediately. This is how professional engineering teams work. Which testing pattern felt most valuable?



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Write unit tests for service functions with pytest
Write integration tests using httpx.AsyncClient with dependency overrides
Mock external services and create reusable test factories
Set up GitHub Actions CI/CD that runs tests on every push
Implement structured logging and Sentry error tracking



Week 6: Docker, Deployment & Production

Days 43–49  |  Phase 2: The Architecture

This Week’s Theme
Your APIs run on localhost. This week they run on the internet — containerized, deployed, and production-ready.


DAY 43  |  Docker Fundamentals
Objective
Package your API so it runs the same on any machine, anywhere
🎥 Watch
“Docker in 100 Seconds” by Fireship  •  “Docker Tutorial” by TechWorld with Nana (first 25 min)
📚 Read
Docker Getting Started — official Docker walkthrough
Docker for Python — Docker for beginners (comprehensive)
🛠️ Build
Install Docker Desktop
Create a Dockerfile for your Task Manager API: use python:3.12-slim base image
COPY requirements.txt first, then pip install (layer caching — understand WHY this order matters)
Set the start command: CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
Create a .dockerignore file (exclude: venv/, __pycache__/, .env, .git/)
Build the image: docker build -t task-api .
Run the container: docker run -p 8000:8000 task-api
Verify your API works by visiting localhost:8000/docs
Practice: docker ps, docker logs, docker stop, docker rm
🤖 AI Prompt
"Explain Docker layers and caching like packing a suitcase. Why should I copy requirements.txt BEFORE copying source code? What happens to build time if I change one line of code? Show me a before/after Dockerfile with proper layer ordering."



DAY 44  |  Docker Compose — Multi-Container Apps
Objective
Run your API, PostgreSQL, and Redis together with one command
🎥 Watch
“Docker Compose Tutorial” by TechWorld with Nana (15 min)
📚 Read
Docker Compose Quickstart — official Compose tutorial
Compose File Reference — all service configuration options
🛠️ Build
Create docker-compose.yml with 3 services: api, postgres, redis
Configure environment variables for each service
Add volume mounts so PostgreSQL data persists across restarts
Add health checks: pg_isready for Postgres, redis-cli ping for Redis
Use depends_on with conditions so API waits for database to be ready
Create an entrypoint script that runs Alembic migrations before starting the API
Run: docker compose up and verify everything works together
Create a Makefile: make up, make down, make logs, make test, make seed
🤖 AI Prompt
"My Docker Compose services can’t connect. The API says ‘connection refused’ when trying to reach Postgres. Explain Docker networking: why localhost doesn’t work between containers, and how service names replace hostnames."



DAY 45  |  Cloud Deployment
Objective
Deploy your API to the internet so anyone can access it
🎥 Watch
“Deploy to Railway” by Fireship (8 min)
📚 Read
Railway Getting Started — Railway deployment guide
Render Docker Deploy — alternative deployment platform
🛠️ Build
Choose Railway or Render (both have free tiers) and create an account
Connect your GitHub repo for automatic deployments
Set up a managed PostgreSQL database on the platform
Set up a managed Redis instance (or use Upstash free tier)
Configure ALL environment variables in the platform dashboard
Set the start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
Add a release command that runs Alembic migrations on deploy
Test the LIVE API: register a user, login, create data — on the deployed URL
Verify /docs is accessible publicly and works correctly
🤖 AI Prompt
"I’m deploying my FastAPI app for the first time. Give me a pre-deployment checklist: environment variables to set, database migration strategy, health check setup, what to verify after deployment, and the 5 most common deployment mistakes."



DAY 46  |  Environment Management & Production Safety
Objective
Manage dev, staging, and production configurations like a professional
🎥 Watch
“Managing Secrets” by IBM Technology (8 min)
📚 Read
Twelve-Factor Config — environment configuration best practices
GitHub Secrets — securely store CI/CD secrets
🛠️ Build
Set up 3 environment configs using pydantic-settings: development (debug=True, verbose logging), staging (debug=False, test email provider), production (debug=False, real email, minimal logging)
Use .env.dev, .env.staging, .env.prod files locally (none committed to Git)
Update GitHub Actions: add secrets for test database URL and API keys
Update CI/CD: run tests → deploy to staging on push to develop → deploy to production on push to main
Practice a database migration on your deployed app: add a column, deploy, verify
Write a runbook document: “What to do when the API is down” with step-by-step recovery
🤖 AI Prompt
"Explain dev vs staging vs production like a restaurant: test kitchen, soft launch, and opening night. What should be different in each environment? What must be the SAME? Show me a pydantic-settings configuration for all three."



DAY 47  |  Deploy All 3 APIs
Objective
Your entire portfolio is live on the internet
🎥 Watch


📚 Read
Production Deployment Checklist — performance metrics to monitor
🛠️ Build
Deploy the Blog API and URL Shortener API (same process as the Task Manager)
Each API has: its own repo, its own deployed URL, its own database, working /docs
Verify all 3 live APIs: register, login, create data, test key features
Add live API URLs to each project’s README
Create a portfolio summary: 3 deployed APIs with different use cases
Test the URL Shortener end-to-end: shorten a URL, visit the short link, check stats
🤖 AI Prompt
"I have 3 APIs deployed. Give me a post-deployment monitoring checklist: what should I check in the first hour, first day, and first week? What metrics should I watch? How do I know if something breaks at 3am?"



DAY 48  |  BUILD DAY: Production-Ready Portfolio
Objective
All APIs are deployed, documented, tested, and showcased
🎥 Watch


📚 Read


🛠️ Build
Final verification: all 3 APIs running with no errors
All 3 repos have: clean README with live URL, CI/CD badge, tech stack, setup instructions
All /docs pages are publicly accessible and well-organized
Sentry is tracking errors on at least 2 APIs
GitHub profile shows all 3 repos with descriptions
Update LinkedIn: add “Backend Developer” and list your deployed projects
🤖 AI Prompt
"Review my 3 deployed APIs as a hiring manager. Task Manager, Blog API, URL Shortener — each with auth, database, testing, and Docker. Is this enough to demonstrate backend engineering capability? What would make this portfolio unbeatable?"



DAY 49  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 6 Reflection:
You have 3 APIs running on the internet. Dockerized, deployed, with CI/CD. Anyone can visit your /docs URLs and test your endpoints. Send one of those URLs to someone today. This is real.



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Write a Dockerfile with proper layer caching
Use Docker Compose to orchestrate API + database + Redis
Deploy to a cloud platform with proper environment configuration
Manage multiple environments (dev, staging, production)
Have 3 APIs live on the internet with public documentation



Week 7: Capstone: AI-Powered Backend

Days 50–56  |  Phase 2: The Architecture

This Week’s Theme
Your final project integrates everything you’ve learned PLUS an AI component. This is the project that makes hiring managers stop scrolling.


DAY 50  |  Project Planning & AI Integration Design
Objective
Design a backend that solves a real problem and includes an AI-powered feature
🎥 Watch
“Building AI Apps with Python” by Fireship (10 min)
📚 Read
Anthropic Python SDK — Claude API quickstart
OpenAI Python Quickstart — alternative AI API
🛠️ Build
Choose your capstone idea (pick one that includes an AI feature):
Example ideas: Smart Notes API (AI summarization + tag suggestion), Job Tracker (AI resume-to-job matching), Content Platform (AI-generated descriptions), Customer Support API (AI auto-responses), Inventory System (AI demand prediction)
Design the full system: ERD diagram, endpoint list, auth plan, AI integration points
Identify which endpoints call the AI API and how to handle: latency, cost, rate limits, failures
Sign up for an AI API key (Claude or OpenAI — both have free credits)
Write a project brief: problem, users, features, architecture diagram
Create the repo and set up the project structure
🤖 AI Prompt
"I’m building a [your project] with AI integration. My plan: [describe]. As a staff engineer, review my architecture. Where should the AI call happen (synchronous? background job?)? How do I handle AI API failures gracefully? How do I manage API costs?"



DAY 51  |  Core Setup — Database, Auth, Base Endpoints
Objective
Set up the foundation using patterns you’ve mastered — this should be fast now
🎥 Watch


📚 Read


🛠️ Build
Set up: FastAPI + SQLAlchemy + Alembic + pydantic-settings
Define all models with relationships and run migrations
Implement auth: register, login, JWT, refresh tokens
Build the base CRUD endpoints for your core resources
Create a seed script with realistic test data
Verify everything works in /docs
This should take your full hour but feel FAST — the patterns are muscle memory now
🤖 AI Prompt
"I’m setting up my capstone. Help me create a setup checklist so I don’t forget anything: project structure, config, database, auth, error handling, logging, health check. I want to get the foundation done in 1 day."



DAY 52  |  Core Business Logic
Objective
Build the unique endpoints that make your project valuable
🎥 Watch


📚 Read


🛠️ Build
Build the 3–5 most important endpoints for your project
Implement the business logic that makes your project unique (not just CRUD)
Add proper validation, error handling, and status codes
Test interactively via /docs as you build
Use conventional Git commits throughout
🤖 AI Prompt
"I’m building [your core feature] and I’m stuck on [problem]. Don’t give me the full solution. Give me 3 hints and point me to the right approach. I want to solve it myself."



DAY 53  |  AI Integration
Objective
Add the AI-powered feature that makes your project stand out from every other portfolio project
🎥 Watch


📚 Read
Anthropic Messages API — Claude API reference for message creation
Prompt Engineering Guide — write effective AI prompts
🛠️ Build
Install the AI SDK: pip install anthropic (or pip install openai)
Create an AI service module: app/services/ai_service.py
Write a function that sends a prompt to the AI API and returns the response
Integrate the AI call into your endpoint: e.g., POST /notes/{id}/summarize calls AI to summarize the note’s content
Handle AI-specific edge cases: API timeout, rate limiting, empty responses, content filtering
Use background tasks for slow AI operations (return 202 with a job ID)
Add caching: if the same content is summarized again, return the cached result
NEVER send sensitive user data to the AI API without explicit consent
Store AI results in the database so they’re not regenerated unnecessarily
🤖 AI Prompt
"I’m integrating the Claude API into my FastAPI backend. Show me: how to structure the API call, handle timeouts (what if Claude takes 30 seconds?), implement retry logic, and cache AI responses. Also: how do I write effective system prompts for consistent output?"



DAY 54  |  Testing, Security & Polish
Objective
Make your capstone production-grade with tests, security, and clean code
🎥 Watch


📚 Read
OWASP API Security — security checklist for APIs
🛠️ Build
Write 15+ tests: unit tests for services, integration tests for endpoints, mock the AI API in tests
Set up GitHub Actions CI with PostgreSQL service container
Security review: rate limiting on AI endpoints (expensive!), input validation, auth on all routes
Add Dockerfile and docker-compose.yml
Clean all code: consistent naming, docstrings on services, remove debug prints
Run Lighthouse/aXe on your /docs page if applicable
🤖 AI Prompt
"My capstone uses a paid AI API. How do I protect against abuse? Show me: rate limiting per user, request cost tracking, setting daily spend limits, and how to gracefully degrade if the AI budget is exceeded."



DAY 55  |  Deploy, Document & Ship
Objective
Your AI-powered backend is live on the internet — the crown jewel of your portfolio
🎥 Watch


📚 Read
README Generator — create a beautiful README
🛠️ Build
Deploy to Railway/Render with all environment variables (including AI API key)
Verify the AI feature works on the deployed version
Write a comprehensive README: project overview, problem it solves, architecture diagram, tech stack (highlight AI integration), features, API docs link, how to run locally, how to run tests
Record a 2-minute Loom video demo of the API in action (showing /docs + AI feature)
Pin the repo on GitHub with a compelling description
Write a LinkedIn post: “I built an AI-powered backend API from scratch...”
🤖 AI Prompt
"Help me write a LinkedIn post about my AI-powered capstone project. I built [describe] from scratch using FastAPI, PostgreSQL, Redis, and the Claude/OpenAI API. I want to highlight: the technical architecture, the AI integration, and what I learned. Target: recruiters and tech professionals."



DAY 56  |  REST & REFLECT
Step away from code. Your brain consolidates architectural patterns during rest.
Week 7 Reflection:
You just built an AI-powered backend system from an empty folder. Auth, database, file uploads, email, caching, AI integration, tests, CI/CD, Docker, deployed to the cloud. This is not a bootcamp project. This is a production system. When did you realize you could actually do this?



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
Design and build a complete backend independently from scratch
Integrate an AI API with proper error handling, caching, and cost management
Write comprehensive tests including mocking external AI services
Deploy a Dockerized application with CI/CD
Document and present the project professionally



Week 8: Phase 2 Wrap-Up — Ship, Reflect, Prepare

Days 57–60  |  Phase 2: The Architecture

This Week’s Theme
Final sprint. 4 APIs in your portfolio. Everything polished, deployed, and documented. You walk into Phase 3 as a backend engineer.


DAY 57  |  GitHub Profile & Portfolio Overhaul
Objective
Make your GitHub tell the story of a job-ready backend engineer
🎥 Watch


📚 Read
Standout GitHub Profiles — profile inspiration
🛠️ Build
Create/update your GitHub profile README: intro, tech stack badges (Python, FastAPI, SQLAlchemy, PostgreSQL, Redis, Docker, pytest), featured projects, GitHub stats
Pin your 4 best repos: Task Manager, Blog API, URL Shortener, AI-Powered Capstone
Every pinned repo has: description, topic tags, live /docs URL in the About section
Add CI badges to every README (tests passing, coverage %)
Clean up any old/messy repos (make private or delete)
Your profile should communicate: “This person builds production backend systems.”
🤖 AI Prompt
"Review my GitHub profile as a recruiter looking for a Python backend developer. Here’s what I have: [describe]. What impression do I get in 10 seconds? What’s missing? What would make you schedule an interview?"



DAY 58  |  Build in Public — Your Engineering Story
Objective
Tell the world what you built and establish your technical voice
🎥 Watch


📚 Read
Learning in Public — the definitive essay on building in public
🛠️ Build
Write and publish a technical article: “How I Built 4 Production APIs in 50 Days with Python & FastAPI”
Include: your architecture decisions, the AI integration challenge, testing strategy, deployment pipeline, what you’d do differently
Publish on DEV.to, Hashnode, or Medium
Write a LinkedIn post linking to the article and sharing your live API URLs
Share with 3 people for feedback and implement their top suggestion
🤖 AI Prompt
"Help me structure a technical blog post about building my backend portfolio. I want to cover: Python/FastAPI patterns I developed, the AI integration (most interesting), testing with dependency overrides, and Docker deployment. Make it educational for others, not just a diary."



DAY 59  |  Skills Gap Analysis & Phase 3 Planning
Objective
Know exactly where you stand and what comes next
🎥 Watch


📚 Read
Backend Developer Roadmap — check off everything you now know
🛠️ Build
Create your Transformation Map: every technology (Python, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Redis, Docker, pytest, GitHub Actions, Sentry, Claude/OpenAI API)
Every concept (REST, auth, JWT, RBAC, caching, background jobs, testing, CI/CD, Docker, deployment)
Every project with live URLs and GitHub links
Look at 5 backend developer job postings (Ghana + international remote)
Highlight every requirement you now meet — circle the gaps
This map IS your Phase 3 strategy
🤖 AI Prompt
"Here’s everything I know and have built: [paste your map]. Compare to mid-level Python backend developer job postings. What are my strengths? What gaps should Phase 3 focus on? Should I learn: message queues, GraphQL, microservices, or something else? Prioritize."



DAY 60  |  Phase 2 Complete — You Are a Backend Engineer
Objective
Celebrate. You earned this.
🎥 Watch


📚 Read


🛠️ Build
Re-read your Day 8 Python refresher code. Then open your AI-powered capstone. The distance between those two files is the proof.
Update your LinkedIn headline to include “Backend Developer | Python | FastAPI”
Send your best live API /docs URL to someone and say: “I built this.”
Write 3 sentences: what you were 52 days ago, what you did, and what you are now.
You have 4 production APIs, an AI integration, automated tests, Docker containers, and cloud deployments.
You’re not learning to code. You’re an engineer who ships.
🤖 AI Prompt
"52 days ago I was refreshing Python basics. Now I have 4 deployed APIs including one with AI integration. Help me write a LinkedIn summary that positions me as a Python backend developer. My background is [your background]. Make it confident, specific, and authentic."



WEEKLY CHECKPOINT
Confirm you can do these before moving on:
GitHub profile tells a clear backend engineering story with 4+ quality repos
Published a technical article about your backend journey
Can identify strengths and gaps against real job postings
All 4 APIs are live, tested, documented, and deployed
LinkedIn reflects your new identity as a backend engineer



Phase 2 Complete.

52 days ago, you were refreshing Python basics.

Today you have 4 production APIs deployed to the internet — including one powered by AI. You’ve written SQL queries, designed database schemas, implemented JWT authentication, built refresh token rotation, uploaded files to the cloud, sent emails, cached with Redis, written 50+ automated tests, set up CI/CD pipelines, containerized with Docker, and deployed to the cloud.

You don’t just know Python. You build systems with it.

You’re a backend engineer.

What’s Next: Phase 3 — The Proof (Days 61–75)
Phase 2 gave you the skills and the projects. Phase 3 turns them into your Shadow Portfolio — projects that solve REAL problems using the Problem → Solution → Impact framework. This is the difference between “I can code” and “Hire me.”



“You don’t need a certificate. You need receipts.”

— Racheal Kuranchie


The Pivot Blueprint © 2026 | thepivotblueprint.com
