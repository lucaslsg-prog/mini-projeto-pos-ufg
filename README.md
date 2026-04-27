# ✅ To-Do List – FastAPI + React + PostgreSQL (Backend em Docker)

Este projeto implementa uma **micro API de gerenciamento de tarefas (to-do list)** utilizando uma arquitetura simples e organizada, agora com:

- ✅ **Backend FastAPI rodando em Docker**
- ✅ **PostgreSQL em container Docker**
- ✅ **Frontend React rodando localmente**

O objetivo desta versão é garantir **ambiente reproduzível**, facilidade de setup e maior proximidade com cenários reais de produção.

---

## 🚀 Tecnologias utilizadas

### Backend
- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- Uvicorn

### Frontend
- React
- Vite
- Axios

### Infraestrutura
- Docker
- Docker Compose

---

## 📂 Estrutura do projeto

```text
todo-app/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   └── task_model.py
│   │   ├── repositories/
│   │   │   └── task_repository.py
│   │   ├── services/
│   │   │   └── task_service.py
│   │   ├── controllers/
│   │   │   └── task_controller.py
│   │   └── schemas/
│   │       └── task_schema.py
│   │
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── api.js
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── index.html
│   └── package.json
│
├── docker-compose.yml
└── README.md
```

---

## 🐳 Docker Compose (Banco + Backend)

Nesta versão, **PostgreSQL e Backend FastAPI são executados juntos via Docker Compose**.

### Arquivo `docker-compose.yml`

```yaml
version: "3.8"

services:
  postgres:
    image: postgres
    container_name: todo-postgres
    environment:
      POSTGRES_DB: todo_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build:
      context: ./backend
    container_name: todo-backend
    depends_on:
      - postgres
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    volumes:
      - ./backend/app:/app/app

volumes:
  postgres_data:
```

---

## ⚙️ Configuração do Backend (Docker)

### Variável de ambiente

Arquivo `backend/.env`:

```env
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/todo_db
```

> ⚠️ Importante:  
> Dentro do Docker, o host do banco é o **nome do serviço (`postgres`)**, e não `localhost`.

---

### Dockerfile do backend

Arquivo `backend/Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY .env .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ▶️ Subindo o ambiente completo

Na raiz do projeto (`todo-app`):

```bash
docker-compose up --build
```

### Serviços disponíveis

- ✅ **Backend FastAPI** → http://localhost:8000
- ✅ **Swagger UI** → http://localhost:8000/docs
- ✅ **Banco PostgreSQL** → localhost:5432

---

## 🌐 Execução do Frontend (local)

O frontend continua rodando **fora do Docker**.

```bash
cd frontend
npm install
npm run dev
```

Frontend disponível em:

- 👉 http://localhost:5173

---

## 🔗 Comunicação Frontend ↔ Backend

O frontend se comunica com o backend via Axios:

```js
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000"
});

export default api;
```

O CORS já está configurado no backend para permitir acesso do frontend.

---

## ✅ Funcionalidades

- Criar tarefas
- Listar tarefas
- Marcar tarefas como concluídas
- Remover tarefas

---

## 🧠 Observações importantes

- O banco de dados é persistido via volume Docker
- As tabelas são criadas automaticamente pelo SQLAlchemy
- Alterações no código do backend refletem automaticamente (volume mapeado)

---

## 📌 Próximos passos

- Dockerizar o frontend
- Criar ambientes `dev` e `prod`
- Adicionar migrations com Alembic
- Implementar autenticação
- Preparar deploy em cloud

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo e prática com FastAPI, Docker, PostgreSQL e React para criar experiencia com desenvolvimento de software assistido por IA na pós graduação da UFG.
