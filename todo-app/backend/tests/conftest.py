import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.main import app
from app.controllers.task_controller import get_db
from app.database import engine  # usa o mesmo engine (Postgres)

# usa o mesmo banco do container
TestingSessionLocal = sessionmaker(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    # limpa o banco antes de cada teste
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
