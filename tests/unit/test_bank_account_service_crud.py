from decimal import Decimal

import pytest

from app.core.exceptions import ConflictError, NotFoundError
from app.models.bank_account import BankAccount
from app.models.user import User
from app.repos.bank_account_repo import BankAccountRepository
from app.services.bank_account_service import BankAccountService

# Data user dummy untuk testing
def create_user(db_session, email="user@example.com"):
    user = User(
        email=email,
        hashed_password="hashed-password",
        full_name="Test User",
        is_active=True,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

# Data rekening bank dummy untuk testing
def create_bank_account(
    db_session,
    user_id,
    account_number="123456789",
):
    account = BankAccount(
        account_number=account_number,
        account_name="Test Account",
        bank_name="BCA",
        balance=Decimal("100000.00"),
        user_id=user_id,
    )
    db_session.add(account)
    db_session.commit()
    db_session.refresh(account)
    return account

# create sukses → data tersimpan, account_number benar
def test_create_success(db_session):
    user = create_user(db_session)

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    account = service.create_account(
        account_number="123456789",
        account_name="Test Account",
        bank_name="BCA",
        balance=Decimal("100000.00"),
        user_id=user.id,
    )

    assert account.id is not None
    assert account.account_number == "123456789"
    assert account.user_id == user.id

# create dengan account_number duplikat → ConflictError
def test_create_duplicate_account_number(db_session):
    user = create_user(db_session)

    create_bank_account(
        db_session,
        user.id,
        "123456789",
    )

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    with pytest.raises(ConflictError):
        service.create_account(
            account_number="123456789",
            account_name="Another Account",
            bank_name="BCA",
            balance=Decimal("200000.00"),
            user_id=user.id,
        )

# update sukses → field berubah
def test_update_success(db_session):
    user = create_user(db_session)

    account = create_bank_account(
        db_session,
        user.id,
    )

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    updated = service.update_account(
        account_id=account.id,
        user_id=user.id,
        account_name="Updated Account",
        bank_name="Mandiri",
        balance=Decimal("500000.00"),
    )

    assert updated.account_name == "Updated Account"
    assert updated.bank_name == "Mandiri"
    assert updated.balance == Decimal("500000.00")

# update akun milik user lain → NotFoundError
def test_update_account_belongs_to_other_user(db_session):
    user1 = create_user(
        db_session,
        "user1@example.com",
    )

    user2 = create_user(
        db_session,
        "user2@example.com",
    )

    account = create_bank_account(
        db_session,
        user1.id,
    )

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    with pytest.raises(NotFoundError):
        service.update_account(
            account_id=account.id,
            user_id=user2.id,
            account_name="Hacked",
            bank_name="BCA",
            balance=Decimal("999999.00"),
        )

# update id tidak ada → NotFoundError
def test_update_account_not_found(db_session):
    user = create_user(db_session)

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    with pytest.raises(NotFoundError):
        service.update_account(
            account_id=99999,
            user_id=user.id,
            account_name="Test",
            bank_name="BCA",
            balance=Decimal("100000.00"),
        )

# delete sukses → akun hilang dari list
def test_delete_success(db_session):
    user = create_user(db_session)

    account = create_bank_account(
        db_session,
        user.id,
    )

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    service.delete_account(
        account_id=account.id,
        user_id=user.id,
    )

    result = service.list_accounts(user.id)

    assert result == []

# delete akun milik user lain → NotFoundError
def test_delete_account_belongs_to_other_user(db_session):
    user1 = create_user(
        db_session,
        "user1@example.com",
    )

    user2 = create_user(
        db_session,
        "user2@example.com",
    )

    account = create_bank_account(
        db_session,
        user1.id,
    )

    service = BankAccountService(
        BankAccountRepository(db_session)
    )

    with pytest.raises(NotFoundError):
        service.delete_account(
            account_id=account.id,
            user_id=user2.id,
        )