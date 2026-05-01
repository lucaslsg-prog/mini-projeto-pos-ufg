from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks/", json={"title": "Minha task"})

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Minha task"
    assert "id" in data
    assert data["completed"] is False  # check default state


def test_list_tasks():
    client.post("/tasks/", json={"title": "Task 1"})

    response = client.get("/tasks/")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Task 1"


def test_complete_task():
    create = client.post("/tasks/", json={"title": "Completar"})
    task_id = create.json()["id"]

    response = client.put(f"/tasks/{task_id}/complete")

    assert response.status_code == 200

    tasks = client.get("/tasks/").json()
    task = next((t for t in tasks if t["id"] == task_id), None)

    assert task is not None
    assert task["completed"] is True


def test_delete_task():
    create = client.post("/tasks/", json={"title": "Deletar"})
    task_id = create.json()["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"

    tasks = client.get("/tasks/").json()
    ids = [t["id"] for t in tasks]

    assert task_id not in ids


def test_complete_task_not_found():
    response = client.put("/tasks/999/complete")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


def test_delete_task_not_found():
    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"