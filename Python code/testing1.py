tasks = {
    1: {"task": "Buy groceries", "completed": False},
    2: {"task": "Submit assignment", "completed": False},
}

# Accessing tasks
for task_id, details in tasks.items():
    print(f"Task {task_id}: {details['task']} - {'Done' if details['completed'] else 'Pending'}")
