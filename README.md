# TaskFlow API

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138.1-009688)
![License](https://img.shields.io/badge/license-MIT-green)

Professional task management API built with **FastAPI**, **SQLAlchemy 2.0** (async), **PostgreSQL**, **Docker**, and **JWT authentication** (coming soon).

> **Status:** Core infrastructure ready – DB connected, health endpoint working, tests passing.

## Features (Current & Upcoming)

- ⬜ User registration and login (JWT) – *in progress*
- ⬜ CRUD for tasks with pagination and filtering – *in progress*
- ✅ Health check endpoint with database verification
- ✅ Asynchronous PostgreSQL with SQLAlchemy 2.0
- ✅ Alembic migrations
- ✅ Docker & Docker Compose for development
- ⬜ Role-based permissions
- ⬜ File uploads
- ⬜ Background tasks and notifications

## Tech Stack

- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **Database:** PostgreSQL 15 (local via Docker, production via Supabase)
- **ORM:** SQLAlchemy 2.0 (async), Alembic
- **Authentication:** JWT (coming soon)
- **Testing:** Pytest, HTTPX
- **DevOps:** Docker, Docker Compose, GitHub Actions (CI/CD)

## Getting Started

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for Windows/Mac)
- [Git](https://git-scm.com/)

### 1. Clone the repository
```bash
git clone https://github.com/Codersnake01/taskflow-api.git
cd taskflow-api
```

### 2. Configure environment 
Copy the example file and adjust if needed:
```bash
cp .env.example .env
```
Default .env works out-of-the-box for local development with Docker.

### 3. Run with Docker
The API will be available at http://localhost:8000.
```bash
docker-compose up --build
```

### 4. Apply database migrations (inside the container)
Open a second terminal while Docker is running:
```bash
docker-compose exec web alembic upgrade head
```

### 5. Verify the health 
```bash
curl http://localhost:8000/api/v1/health
```
Expected response: `{"status":"ok","database":"connected"}`

## Running Tests
```bash
# Install dev dependencies (if not already)
uv sync

# Run tests
uv run pytest
```

## Project Structure
```
taskflow-api/
├── app/
│   ├── api/v1/endpoints/   # Route handlers
│   ├── core/               # Configuration (Pydantic Settings)
│   ├── db/                 # Database engine, session, base
│   └── models/             # SQLAlchemy models
├── tests/                  # Unit tests
├── alembic/                # Database migrations
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## License

This project is licensed under the MIT License. See LICENSE file for details.