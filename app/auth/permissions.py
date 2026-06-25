from enum import Enum
from app.schemas.user_schema import UserRole


class Resource(str, Enum):
    users = "users"
    projects = "projects"
    tasks = "tasks"


class Action(str, Enum):
    create = "create"
    read = "read"
    update = "update"
    delete = "delete"
    assign = "assign"


PERMISSIONS: dict[UserRole, dict[Resource, set[Action]]] = {
    UserRole.admin: {
        Resource.users: {Action.create, Action.update, Action.read, Action.delete},
        Resource.projects: {Action.create, Action.read, Action.update, Action.delete},
        Resource.tasks: {
            Action.create,
            Action.read,
            Action.update,
            Action.delete,
            Action.assign,
        },
    },
    UserRole.manager: {
        Resource.users: {Action.read},
        Resource.projects: {Action.create, Action.read, Action.update, Action.delete},
        Resource.tasks: {
            Action.create,
            Action.read,
            Action.update,
            Action.delete,
            Action.assign,
        },
    },
    UserRole.member: {
        Resource.users: {Action.read},
        Resource.projects: {Action.read},
        Resource.tasks: {Action.create, Action.read, Action.update, Action.delete},
    },
}
