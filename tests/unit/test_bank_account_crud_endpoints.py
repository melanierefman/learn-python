# Helper untuk to login dan register
def register_and_login(client, email):
    client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "password": "supersecret",
            "full_name": "Test User",
        },
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": email,
            "password": "supersecret",
        },
    )

    return response.json()["access_token"]


# POST create → 201
def test_create_bank_account(client):
    token = register_and_login(
        client,
        "user@example.com",
    )

    response = client.post(
        "/api/v1/bank-accounts",
        headers={
            "Authorization": f"Bearer {token}",
        },
        json={
            "account_number": "123456789",
            "account_name": "My BCA",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["account_number"] == "123456789"
    assert data["account_name"] == "My BCA"
    assert data["bank_name"] == "BCA"
    assert data["user_id"] is not None
    assert "hashed_password" not in data
    
    
# POST create duplikat → 409
def test_create_duplicate_bank_account(client):
    token = register_and_login(
        client,
        "duplicate@example.com",
    )

    payload = {
        "account_number": "999999999",
        "account_name": "My Account",
        "bank_name": "BCA",
        "balance": 100000,
    }

    headers = {
        "Authorization": f"Bearer {token}",
    }

    first = client.post(
        "/api/v1/bank-accounts",
        headers=headers,
        json=payload,
    )

    assert first.status_code == 201

    second = client.post(
        "/api/v1/bank-accounts",
        headers=headers,
        json=payload,
    )

    assert second.status_code == 409
   
    
# POST create tanpa token → 401
def test_create_bank_account_without_token(client):
    response = client.post(
        "/api/v1/bank-accounts",
        json={
            "account_number": "123456789",
            "account_name": "My BCA",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert response.status_code == 401
 
    
# PUT update → 200, field berubah
def test_update_bank_account(client):
    token = register_and_login(
        client,
        "update@example.com",
    )

    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Create account terlebih dahulu
    create_response = client.post(
        "/api/v1/bank-accounts",
        headers=headers,
        json={
            "account_number": "111111111",
            "account_name": "My BCA",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert create_response.status_code == 201

    account_id = create_response.json()["id"]

    # Update account
    response = client.put(
        f"/api/v1/bank-accounts/{account_id}",
        headers=headers,
        json={
            "account_name": "Updated BCA",
            "bank_name": "Mandiri",
            "balance": 500000,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["account_name"] == "Updated BCA"
    assert data["bank_name"] == "Mandiri"
    assert data["balance"] == "500000.00"
    assert data["account_number"] == "111111111"


# PUT update akun user lain → 404
def test_update_bank_account_other_user(client):
    # User 1 membuat rekening
    token_user1 = register_and_login(
        client,
        "user1@example.com",
    )

    headers_user1 = {
        "Authorization": f"Bearer {token_user1}",
    }

    create_response = client.post(
        "/api/v1/bank-accounts",
        headers=headers_user1,
        json={
            "account_number": "222222222",
            "account_name": "User 1 Account",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert create_response.status_code == 201

    account_id = create_response.json()["id"]

    # User 2 login
    token_user2 = register_and_login(
        client,
        "user2@example.com",
    )

    headers_user2 = {
        "Authorization": f"Bearer {token_user2}",
    }

    # User 2 mencoba update rekening User 1
    response = client.put(
        f"/api/v1/bank-accounts/{account_id}",
        headers=headers_user2,
        json={
            "account_name": "Hacked Account",
            "bank_name": "Mandiri",
            "balance": 999999,
        },
    )

    assert response.status_code == 404


# PUT dengan balance negatif → 422
def test_update_bank_account_negative_balance(client):
    token = register_and_login(
        client,
        "negative@example.com",
    )

    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Create account
    create_response = client.post(
        "/api/v1/bank-accounts",
        headers=headers,
        json={
            "account_number": "333333333",
            "account_name": "My Account",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert create_response.status_code == 201

    account_id = create_response.json()["id"]

    # Update dengan balance negatif
    response = client.put(
        f"/api/v1/bank-accounts/{account_id}",
        headers=headers,
        json={
            "account_name": "Updated Account",
            "bank_name": "BCA",
            "balance": -50000,
        },
    )

    assert response.status_code == 422


# DELETE → 204
def test_delete_bank_account(client):
    token = register_and_login(
        client,
        "delete@example.com",
    )

    headers = {
        "Authorization": f"Bearer {token}",
    }

    # Create account
    create_response = client.post(
        "/api/v1/bank-accounts",
        headers=headers,
        json={
            "account_number": "444444444",
            "account_name": "Delete Account",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert create_response.status_code == 201

    account_id = create_response.json()["id"]

    # Delete account
    response = client.delete(
        f"/api/v1/bank-accounts/{account_id}",
        headers=headers,
    )

    assert response.status_code == 204


# DELETE akun user lain → 404
def test_delete_bank_account_other_user(client):
    # User 1 membuat rekening
    token_user1 = register_and_login(
        client,
        "owner@example.com",
    )

    headers_user1 = {
        "Authorization": f"Bearer {token_user1}",
    }

    create_response = client.post(
        "/api/v1/bank-accounts",
        headers=headers_user1,
        json={
            "account_number": "555555555",
            "account_name": "Owner Account",
            "bank_name": "BCA",
            "balance": 100000,
        },
    )

    assert create_response.status_code == 201

    account_id = create_response.json()["id"]

    # User 2 login
    token_user2 = register_and_login(
        client,
        "attacker@example.com",
    )

    headers_user2 = {
        "Authorization": f"Bearer {token_user2}",
    }

    # User 2 mencoba delete rekening User 1
    response = client.delete(
        f"/api/v1/bank-accounts/{account_id}",
        headers=headers_user2,
    )

    assert response.status_code == 404
    
