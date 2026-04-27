from sqlalchemy.orm import Session
from app.models.task_model import Task

class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Task).all()

    def create(self, title: str):
        task = Task(title=title)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def complete(self, task_id: int):
        task = self.db.query(Task).get(task_id)
        task.completed = True
        self.db.commit()
        return task

    def delete(self, task_id: int):
        task = self.db.query(Task).get(task_id)
        self.db.delete(task)
        self.db.commit()