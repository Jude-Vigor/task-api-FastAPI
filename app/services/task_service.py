tasks = []


def create_task(task_data):
    new_task = {
        "id": len(tasks) + 1,
        "title": task_data.title,
        "description": task_data.description,
        "status": task_data.status,
        "priority": task_data.priority,
        "due_date": task_data.due_date,
    }
    tasks.append(new_task)
    print("TASKS AFTER CREATE:", tasks)
    return new_task


def get_all_tasks(status=None, priority=None, search=None, sort_by=None, order="asc"):
    filtered_tasks = tasks.copy()
    if status:
        filtered_tasks = [task for task in filtered_tasks if task["status"] == status]
    if priority is not None:
        filtered_tasks = [
            task for task in filtered_tasks if task["priority"] == priority
        ]
    if search:
        search = search.lower()
        filtered_tasks = [
            task
            for task in filtered_tasks
            if search in task["title"].lower()
            or (task["description"] and search in task["description"].lower())
        ]
    if sort_by:
        reverse = order == "desc"
        filtered_tasks.sort(key=lambda task: task[sort_by], reverse=reverse)
    print("INSIDE get_all_tasks")
    return filtered_tasks


def get_task_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id: int, task_data):
    task = get_task_by_id(task_id)

    if not task:
        return None

    task["title"] = task_data.title
    task["description"] = task_data.description
    task["priority"] = task_data.priority
    task["status"] = task_data.status
    task["due_date"] = task_data.due_date

    return task


def delete_task(task_id: int):
    task = get_task_by_id(task_id)

    if not task:
        return False

    tasks.remove(task)
    return True
