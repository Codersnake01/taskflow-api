# TaskFlow API

[![codecov](https://codecov.io/gh/Codersnake01/taskflow-api/branch/main/graph/badge.svg)](https://codecov.io/gh/Codersnake01/taskflow-api)
![CI](https://github.com/Codersnake01/taskflow-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138.1-009688)
![License](https://img.shields.io/badge/license-MIT-green)

Professional task management API built with **FastAPI**, **SQLAlchemy 2.0** (async), **PostgreSQL**, **Docker**, and **JWT authentication**.

> **Live Demo:** [https://taskflow-api-pe4h.onrender.com](https://taskflow-api-pe4h.onrender.com) — Swagger UI with all endpoints.

## Features

- ✅ User registration and login with JWT
- ✅ Full CRUD for tasks (title, description, status, owner)
- ✅ Pagination, filtering by status, and text search
- ✅ Permission control (users only see their own tasks)
- ✅ Health check endpoint with database status
- ✅ Asynchronous PostgreSQL with SQLAlchemy 2.0
- ✅ Alembic migrations
- ✅ Docker & Docker Compose for local development
- ✅ Automated testing (92% coverage)
- ✅ CI/CD pipeline (linting, type checking, tests)
- ✅ Deployed on Render with Supabase PostgreSQL
- ⬜ Role-based permissions (admin/reader)
- ⬜ File uploads
- ⬜ Background tasks and notifications

## Tech Stack

- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **Database:** PostgreSQL 15 (local via Docker, production via Supabase)
- **ORM:** SQLAlchemy 2.0 (async), Alembic
- **Authentication:** JWT (passlib, bcrypt)
- **Cloud:** Render (API), Supabase (PostgreSQL)
- **CI/CD:** GitHub Actions, Codecov
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

### 2. Configure environment variables
Copy the example file and adjust if needed:
```bash
cp .env.example .env
```
Default .env works out-of-the-box for local development with Docker.

### 3. Run with Docker
```bash
docker-compose up --build
```
The API will be available at http://localhost:8000.

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

## Code Quality & CI

- **Linting/Formatting:** Ruff
- **Static Typing:** MyPy
- **CI Pipeline:** GitHub Actions runs on every push:
  - `ruff check`
  - `mypy app`
  - `pytest` with coverage report
  - Coverage uploaded to Codecov (badge above)

## Deployment

The API is automatically deployed on [Render](https://render.com) whenever changes are pushed to `main`.  
The PostgreSQL database is hosted on [Supabase](https://supabase.com).  
A GitHub Actions cron job pings the health endpoint every 6 hours to prevent cold starts on free tiers.

## Project Structure
```
taskflow-api/
├── app/
│ ├── api/v1/endpoints/ # Route handlers (auth, tasks, health)
│ ├── core/ # Configuration, security (JWT, hashing)
│ ├── db/ # Async engine, session
│ ├── models/ # SQLAlchemy models (User, Task)
│ └── schemas/ # Pydantic schemas
├── tests/ # Test suite (auth, tasks, health)
├── alembic/ # Database migrations
├── .github/workflows/ # CI/CD and keep-alive
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## License

This project is licensed under the MIT License. See LICENSE file for details.