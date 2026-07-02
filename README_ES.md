# TaskFlow API

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.138.1-009688)
![License](https://img.shields.io/badge/license-MIT-green)

API profesional de gestión de tareas construida con **FastAPI**, **SQLAlchemy 2.0** (asíncrono), **PostgreSQL**, **Docker** y **autenticación JWT** (próximamente).

> **Estado:** Infraestructura principal lista – base de datos conectada, endpoint de salud funcionando, tests pasando.

## Funcionalidades (actuales y próximas)

- ⬜ Registro e inicio de sesión con JWT – *en progreso*
- ⬜ CRUD de tareas con paginación y filtros – *en progreso*
- ✅ Endpoint de verificación de salud con estado de la base de datos
- ✅ PostgreSQL asíncrono con SQLAlchemy 2.0
- ✅ Migraciones con Alembic
- ✅ Docker & Docker Compose para desarrollo
- ⬜ Roles y permisos
- ⬜ Subida de archivos
- ⬜ Tareas en segundo plano y notificaciones

## Tecnologías

- **Backend:** Python 3.11+, FastAPI, Uvicorn
- **Base de datos:** PostgreSQL 15 (local con Docker, producción con Supabase)
- **ORM:** SQLAlchemy 2.0 (async), Alembic
- **Autenticación:** JWT (próximamente)
- **Testing:** Pytest, HTTPX
- **DevOps:** Docker, Docker Compose, GitHub Actions (CI/CD)

## Primeros pasos

### Requisitos previos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Windows/Mac)
- [Git](https://git-scm.com/)

### 1. Clonar el repositorio
```bash
git clone https://github.com/Codersnake01/taskflow-api.git
cd taskflow-api
```

### 2. Configurar variables de entorno

Copia el archivo de ejemplo y ajusta si es necesario:
```bash
cp .env.example .env
```
El .env por defecto funciona directamente para desarrollo local con Docker.

### 3. Ejecutar con Docker
```bash
docker-compose up --build
```
La API estará disponible en `http://localhost:8000`.

### 4. Aplicar las migraciones de la base de datos (dentro del contenedor)
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
# Instalar dependencias de desarrollo (si no lo has hecho)
uv sync

# Ejecutar tests
uv run pytest
```

## Estructura del Proyecto
```
taskflow-api/
├── app/
│   ├── api/v1/endpoints/   # Manejadores de rutas
│   ├── core/               # Configuración (Pydantic Settings)
│   ├── db/                 # Motor de base de datos, sesión, base
│   └── models/             # Modelos SQLAlchemy
├── tests/                  # Tests unitarios
├── alembic/                # Migraciones de base de datos
├── docker-compose.yml
├── Dockerfile
└── README_ES.md
```

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
