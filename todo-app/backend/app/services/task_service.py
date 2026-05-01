from app.repositories.task_repository import TaskRepository
from fastapi import HTTPException


class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def list_tasks(self):
        return self.repository.get_all()

    def create_task(self, title: str):
        return self.repository.create(title)

    def complete_task(self, task_id: int):
        task = self.repository.complete(task_id)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return task

    def delete_task(self, task_id: int):
        deleted = self.repository.delete(task_id)

        if not deleted:
            raise HTTPException(status_code=404, detail="Task not found")