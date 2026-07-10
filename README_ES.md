# TaskFlow API

[![codecov](https://codecov.io/gh/Codersnake01/taskflow-api/branch/main/graph/badge.svg)](https://codecov.io/gh/Codersnake01/taskflow-api)
![CI](https://github.com/Codersnake01/taskflow-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138.1-009688)
![License](https://img.shields.io/badge/license-MIT-green)

API profesional de gestión de tareas construida con **FastAPI**, **SQLAlchemy 2.0** (asíncrono), **PostgreSQL**, **Docker** y **autenticación JWT**.

> **Demo en vivo:** [https://taskflow-api-pe4h.onrender.com/docs](https://taskflow-api-pe4h.onrender.com/docs) — Swagger UI con todos los endpoints.

## Funcionalidades

- ✅ Registro e inicio de sesión con JWT
- ✅ CRUD completo de tareas (título, descripción, estado, propietario)
- ✅ Paginación, filtros por estado y búsqueda textual
- ✅ Control de permisos (cada usuario ve solo sus tareas)
- ✅ Endpoint de salud con estado de la base de datos
- ✅ PostgreSQL asíncrono con SQLAlchemy 2.0
- ✅ Migraciones con Alembic
- ✅ Docker y Docker Compose para desarrollo local
- ✅ Tests automatizados (cobertura del 92 %)
- ✅ Pipeline CI/CD (linting, verificación de tipos, tests)
- ✅ Desplegado en Render con PostgreSQL en Supabase
- ⬜ Roles y permisos avanzados (admin/lector)
- ⬜ Subida de archivos
- ⬜ Tareas en segundo plano y notificaciones

## Tecnologías

- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **Base de datos:** PostgreSQL 15 (local con Docker, producción con Supabase)
- **ORM:** SQLAlchemy 2.0 (async), Alembic
- **Autenticación:** JWT (passlib, bcrypt)
- **Nube:** Render (API), Supabase (PostgreSQL)
- **CI/CD:** GitHub Actions, Codecov
- **Testing:** Pytest, HTTPX
- **DevOps:** Docker, Docker Compose, GitHub Actions

## Primeros pasos

### Requisitos previos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac)
- [Git](https://git-scm.com/)

### 1. Clonar el repositorio
```bash
git clone https://github.com/Codersnake01/taskflow-api.git
cd taskflow-api
```

### 2. Configurar las variables de entorno
Copia el archivo de ejemplo y ajústalo si es necesario:
```bash
cp .env.example .env
```
El archivo `.env` por defecto funciona para desarrollo local con Docker.

### 3. Ejecutar con Docker
```bash
docker-compose up --build
```
La API estará disponible en `http://localhost:8000`.

### 4. Aplicar las migraciones (dentro del contenedor)
Abre una segunda terminal mientras Docker está corriendo:
```bash
docker-compose exec web alembic upgrade head
```

### 5. Verificar el endpoint de salud
```bash
curl http://localhost:8000/api/v1/health
```
Respuesta esperada: `{"status":"ok","database":"connected"}`

## Ejecutar tests
```bash
# Instalar dependencias de desarrollo (si no se ha hecho ya)
uv sync

# Ejecutar los tests
uv run pytest
```

## Calidad de código e CI

- **Linting/Formateo:** Ruff
- **Tipado estático:** MyPy
- **Pipeline CI:** GitHub Actions se ejecuta en cada push:
  - `ruff check`
  - `mypy app`
  - `pytest` con informe de cobertura
  - Cobertura subida a Codecov (badge arriba)

## Despliegue

La API se despliega automáticamente en [Render](https://render.com) con cada push a `main`.  
La base de datos PostgreSQL está alojada en [Supabase](https://supabase.com).  
Un **keep-alive** de GitHub Actions hace ping al endpoint de salud cada 6 horas para evitar tiempos de arranque en los planes gratuitos.

## Estructura del proyecto

```
taskflow-api/
├── app/
│   ├── api/v1/endpoints/   # Manejadores de rutas (auth, tasks, health)
│   ├── core/               # Configuración, seguridad (JWT, hashing)
│   ├── db/                 # Motor asíncrono, sesión
│   ├── models/             # Modelos SQLAlchemy (User, Task)
│   └── schemas/            # Esquemas Pydantic
├── tests/                  # Suite de tests (auth, tasks, health)
├── alembic/                # Migraciones de base de datos
├── .github/workflows/      # CI/CD y keep-alive
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.