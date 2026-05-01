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
        task = self.db.query(Task).filter(Task.id == task_id).first()

        if not task:
            return None

        task.completed = True
        self.db.commit()
        self.db.refresh(task)

        return task

    def delete(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()

        if not task:
            return False

        self.db.delete(task)
        self.db.commit()

        return True