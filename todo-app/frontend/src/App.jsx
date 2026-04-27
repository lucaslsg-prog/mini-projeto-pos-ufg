import { useEffect, useState } from "react";
import api from "./api";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [title, setTitle] = useState("");

  const loadTasks = async () => {
    const res = await api.get("/tasks/");
    setTasks(res.data);
  };

  const createTask = async () => {
    if (!title.trim()) return;
    await api.post("/tasks/", { title });
    setTitle("");
    loadTasks();
  };

  const toggleTask = async (task) => {
    if (!task.completed) {
      await api.put(`/tasks/${task.id}/complete`);
      loadTasks();
    }
  };

  const deleteTask = async (id) => {
    await api.delete(`/tasks/${id}`);
    loadTasks();
  };

  useEffect(() => {
    loadTasks();
  }, []);

  return (
    <div className="container">
      <h1>📝 To-do List</h1>

      <div className="input-group">
        <input
          type="text"
          placeholder="Adicionar nova tarefa..."
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && createTask()}
        />
        <button onClick={createTask}>Adicionar</button>
      </div>

      <ul className="task-list">
        {tasks.map((task) => (
          <li key={task.id} className={task.completed ? "completed" : ""}>
            <label>
              <input
                type="checkbox"
                checked={task.completed}
                onChange={() => toggleTask(task)}
              />
              <span>{task.title}</span>
            </label>

            <button
              className="delete-btn"
              onClick={() => deleteTask(task.id)}
              title="Excluir tarefa"
            >
              ❌
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;