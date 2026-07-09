import pytest


@pytest.mark.anyio
async def test_create_task(client):
    # Registrar usuario y obtener token
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "tasker@test.com",
            "password": "secret123",
            "full_name": "Tasker",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "tasker@test.com", "password": "secret123"},
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = await client.post(
        "/api/v1/tasks/",
        json={"title": "Mi tarea", "description": "Detalle", "done": False},
        headers=headers,
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Mi tarea"
    assert data["owner_id"] is not None


@pytest.mark.anyio
async def test_get_tasks_pagination(client):
    # Registrar usuario y obtener token
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "pager@test.com",
            "password": "secret123",
            "full_name": "Pager",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "pager@test.com", "password": "secret123"},
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Crear varias tareas
    for i in range(5):
        await client.post(
            "/api/v1/tasks/",
            json={"title": f"Tarea {i}"},
            headers=headers,
        )

    # Listar con límite 2
    response = await client.get("/api/v1/tasks/?limit=2", headers=headers)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 2


@pytest.mark.anyio
async def test_update_task(client):
    # Registrar usuario y obtener token
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "updater@test.com",
            "password": "secret123",
            "full_name": "Updater",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "updater@test.com", "password": "secret123"},
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Crear tarea
    create_resp = await client.post(
        "/api/v1/tasks/",
        json={"title": "Original"},
        headers=headers,
    )
    task_id = create_resp.json()["id"]

    # Actualizar
    response = await client.put(
        f"/api/v1/tasks/{task_id}",
        json={"done": True, "title": "Modificada"},
        headers=headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["done"] is True
    assert data["title"] == "Modificada"


@pytest.mark.anyio
async def test_delete_task(client):
    # Registrar usuario y obtener token
    await client.post(
        "/api/v1/auth/register",
        json={
            "email": "deleter@test.com",
            "password": "secret123",
            "full_name": "Deleter",
        },
    )
    login_resp = await client.post(
        "/api/v1/auth/login",
        data={"username": "deleter@test.com", "password": "secret123"},
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Crear tarea
    create_resp = await client.post(
        "/api/v1/tasks/",
        json={"title": "Para borrar"},
        headers=headers,
    )
    task_id = create_resp.json()["id"]

    # Eliminar
    response = await client.delete(f"/api/v1/tasks/{task_id}", headers=headers)
    assert response.status_code == 204

    # Verificar que ya no existe
    get_resp = await client.get(f"/api/v1/tasks/{task_id}", headers=headers)
    assert get_resp.status_code == 404


@pytest.mark.anyio
async def test_unauthorized_access(client):
    response = await client.get("/api/v1/tasks/")
    assert response.status_code == 401

@pytest.mark.anyio
async def test_get_task_not_found(client):
    # Registrar y obtener token
    await client.post(
        "/api/v1/auth/register",
        json={"email": "nobody@test.com", "password": "secret123", "full_name": "Nobody"},
    )
    login_resp = await client.post(
        "/api/v1/auth/login", data={"username": "nobody@test.com", "password": "secret123"}
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    # Intentar obtener una tarea inexistente
    response = await client.get("/api/v1/tasks/9999", headers=headers)
    assert response.status_code == 404


@pytest.mark.anyio
async def test_create_task_without_token(client):
    response = await client.post("/api/v1/tasks/", json={"title": "Sin token"})
    assert response.status_code == 401