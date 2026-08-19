# Day 26 OWASP API Security Review

This review checks the current Task Management API against common OWASP API Security Top 10 risks.

## What The API Already Handles

### 1. Broken Authentication

Status: Mostly handled

The API uses hashed passwords, JWT access tokens, short access-token expiry, refresh tokens, refresh-token hashing, and refresh-token rotation.

Relevant code:

- `app/auth/security.py`
- `app/routers/auth_router.py`
- `app/services/refresh_token_service.py`

Remaining improvement:

- Add logout/revoke-refresh-token endpoint.
- Consider detecting refresh-token reuse and revoking all tokens for that user.

### 2. Broken Object Level Authorization

Status: Partially handled

Task access is filtered by user role:

- Admins can access all tasks.
- Managers can access tasks in projects they own.
- Members can access their own tasks.

Relevant code:

- `app/services/task_service.py`

Business rule:

- Project reads are broad by design for users with `projects:read`.
- Admins can delete any project.
- Managers can modify only projects they own.
- Members can update only tasks assigned to them.

Remaining improvement:

- User read endpoints allow any role with `users:read` permission to view users by id.

### 3. Broken Function Level Authorization

Status: Handled

Routes use permission dependencies before allowing sensitive actions.

Examples:

- `require_permission(Resource.tasks, Action.create)`
- `require_permission(Resource.projects, Action.delete)`
- `require_role(UserRole.admin, UserRole.manager)` for task assignment

Relevant code:

- `app/auth/dependencies.py`
- `app/auth/permissions.py`
- `app/routers/task_router.py`
- `app/routers/project_router.py`

### 4. Unrestricted Resource Consumption

Status: Partially handled

The API limits pagination size and rate-limits auth routes.

Relevant code:

- `limit: int = Query(10, ge=1, le=100)`
- `@limiter.limit("5/minute")`

Remaining improvement:

- Consider rate limiting more expensive non-auth endpoints too, especially list/search endpoints.

### 5. Excessive Data Exposure

Status: Mostly handled

Response schemas avoid returning `password_hash`. Auth responses return only tokens and token type.

Relevant code:

- `app/schemas/user_schema.py`
- `app/schemas/task_schema.py`
- `app/schemas/project_schema.py`

Remaining improvement:

- Review whether project-with-tasks responses should expose assignee email/role to every allowed project reader.

### 6. Mass Assignment

Status: Partially handled

Some request schemas reject unknown fields with `extra="forbid"`, which helps prevent clients from sneaking in fields like `role`, `owner_id`, or `created_at`.

Relevant code:

- `UserCreate`
- `TaskCreate`
- `TaskAssign`

Remaining improvement:

- Add `extra="forbid"` to update/create schemas that do not have it yet, such as `TaskUpdate`, `ProjectCreate`, and `ProjectUpdate`.

### 7. Security Misconfiguration

Status: Mostly handled

The API now restricts CORS to configured frontend origins and avoids using `*`.

Relevant code:

- `app/main.py`
- `.env`

Remaining improvement:

- Use production-safe environment variables.
- Do not expose docs publicly in production unless intentionally allowed.

## Current Priority Fixes

1. Filter project read endpoints by role/ownership.
2. Add logout or refresh-token revocation.
3. Add `extra="forbid"` to remaining input schemas.
4. Consider refresh-token reuse detection.
5. Consider rate limiting expensive non-auth endpoints.
