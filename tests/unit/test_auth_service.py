# Latihan 1A

import pytest

from app.core.exceptions import (
    ConflictError,
    InvalidCredentialsError,
    UnauthorizedError,
)
from app.repos.user_repo import UserRepository
from app.services.auth_service import AuthService


def test_register_success(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    user = service.register(
        email="user@example.com",
        password="supersecret",
        full_name="Test User",
    )

    assert user.id is not None
    assert user.email == "user@example.com"
    assert user.hashed_password != "supersecret"
    assert user.is_active is True


def test_register_email_uppercase_saved_lowercase(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    user = service.register(
        email="USER@EXAMPLE.COM",
        password="supersecret",
    )

    assert user.email == "user@example.com"


def test_register_duplicate_email(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    service.register(
        email="user@example.com",
        password="supersecret",
    )

    with pytest.raises(ConflictError):
        service.register(
            email="user@example.com",
            password="anotherpassword",
        )


def test_authenticate_success(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    registered_user = service.register(
        email="user@example.com",
        password="supersecret",
    )

    user = service.authenticate(
        email="user@example.com",
        password="supersecret",
    )

    assert user.id == registered_user.id
    assert user.email == "user@example.com"


def test_authenticate_wrong_password(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    service.register(
        email="user@example.com",
        password="supersecret",
    )

    with pytest.raises(InvalidCredentialsError):
        service.authenticate(
            email="user@example.com",
            password="wrongpassword",
        )


def test_authenticate_unknown_email(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    with pytest.raises(InvalidCredentialsError):
        service.authenticate(
            email="unknown@example.com",
            password="supersecret",
        )


def test_issue_token_and_get_user_from_token(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    user = service.register(
        email="user@example.com",
        password="supersecret",
    )

    token = service.issue_token(user)

    result = service.get_user_from_token(token)

    assert result.id == user.id


def test_get_user_from_invalid_token(db_session):
    user_repo = UserRepository(db_session)
    service = AuthService(user_repo)

    with pytest.raises(UnauthorizedError):
        service.get_user_from_token("invalid-token")