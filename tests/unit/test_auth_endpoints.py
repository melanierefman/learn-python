def test_register_success(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "supersecret",
            "full_name": "Test User",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "user@example.com"
    assert data["full_name"] == "Test User"
    assert "hashed_password" not in data


def test_register_duplicate_email(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "supersecret",
        },
    )

    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "anotherpassword",
        },
    )

    assert response.status_code == 409


def test_register_password_too_short(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "1234567",
        },
    )

    assert response.status_code == 422


def test_login_success(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "supersecret",
        },
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "user@example.com",
            "password": "supersecret",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "password": "supersecret",
        },
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "user@example.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401


def test_get_bank_accounts_without_token(client):
    response = client.get("/api/v1/bank-accounts")

    assert response.status_code == 401