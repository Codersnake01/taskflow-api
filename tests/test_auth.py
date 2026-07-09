import pytest


@pytest.mark.anyio
async def test_register(client):
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "secret123",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.anyio
async def test_register_duplicate(client):
    # Registra el mismo email dos veces
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@example.com",
            "password": "secret123",
            "full_name": "Test User",
        },
    )
    response = await client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "other", "full_name": "Dup"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


@pytest.mark.anyio
async def test_login_success(client):
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "login@test.com",
            "password": "secret123",
            "full_name": "Login Test",
        },
    )
    response = await client.post(
        "/api/v1/auth/login",
        data={"username": "login@test.com", "password": "secret123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


@pytest.mark.anyio
async def test_login_invalid_credentials(client):
    response = await client.post(
        "/api/v1/auth/login", data={"username": "noexist@test.com", "password": "wrong"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
