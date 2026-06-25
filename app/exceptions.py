class TaskNotFoundException(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id
        self.message = f"Task with id {task_id} not found"
        super().__init__(self.message)


class DatabaseIntegrityException(Exception):
    def __init__(self, message: str = "Database constraint violation"):
        self.message = message
        super().__init__(self.message)


class AuthorizationException(Exception):
    def __init__(self, message: str = "Not permitted"):
        self.message = message
        super().__init__(self.message)
