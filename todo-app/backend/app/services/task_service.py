from app.repositories.task_repository import TaskRepository

class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def list_tasks(self):
        return self.repository.get_all()

    def create_task(self, title: str):
        return self.repository.create(title)

    def complete_task(self, task_id: int):
        return self.repository.complete(task_id)

    def delete_task(self, task_id: int):
        self.repository.delete(task_id)