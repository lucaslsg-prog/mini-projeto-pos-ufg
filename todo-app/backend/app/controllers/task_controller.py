from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.task_service import TaskService
from app.repositories.task_repository import TaskRepository
from app.schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    return service.list_tasks()

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    return service.create_task(task.title)

@router.put("/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    return service.complete_task(task_id)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    service = TaskService(TaskRepository(db))
    service.delete_task(task_id)
    return {"message": "Task deleted"}