from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.exceptions import AppException, app_exception_handler

app = FastAPI(
    title="TaskFlow API",
    description="API de gestión de tareas con autenticación JWT",
    version="0.1.0",
)

app.include_router(api_router, prefix="/api/v1")

app.add_exception_handler(AppException, app_exception_handler)
