import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.db.session import get_db
from unittest.mock import AsyncMock

# Mock de la sesión que simula execute sin error
async def mock_db():
    session = AsyncMock()
    session.execute = AsyncMock(return_value=None)
    yield session

@pytest.mark.anyio
async def test_health_check():
    app.dependency_overrides[get_db] = mock_db

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/v1/health")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "connected"

    # Limpiar el override
    app.dependency_overrides.clear()