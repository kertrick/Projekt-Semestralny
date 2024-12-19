from django.shortcuts import get_object_or_404
from .models import Task

# CREATE
def create_task(user, text, is_completed=False):
    task = Task.objects.create(user=user, text=text, is_completed=is_completed)
    return task

# READ (Get all tasks for a user)
def get_tasks_for_user(user):
    return Task.objects.filter(user=user)

# READ (Get a single task by ID)
def get_task_by_id(task_id, user):
    return get_object_or_404(Task, id=task_id, user=user)

# UPDATE
def update_task(task_id, user, text=None, is_completed=None):
    task = get_object_or_404(Task, id=task_id, user=user)
    if text is not None:
        task.text = text
    if is_completed is not None:
        task.is_completed = is_completed
    task.save()
    return task

# DELETE
def delete_task(task_id, user):
    task = get_object_or_404(Task, id=task_id, user=user)
    task.delete()
    return True
