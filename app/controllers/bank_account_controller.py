from typing import Annotated

from fastapi import APIRouter, Query, Response, status

from app.deps import CurrentUser, DbDep
from app.repos.bank_account_repo import BankAccountRepository
from app.schemas.bank_account import (
    BankAccountCreate,
    BankAccountResponse,
    BankAccountUpdate,
)
from app.services.bank_account_service import BankAccountService

router = APIRouter(prefix="/bank-accounts", tags=["bank-accounts"])


@router.get(
    "",
    response_model=list[BankAccountResponse],
    summary="Get all bank accounts of current user",
)
def list_bank_accounts(
    db: DbDep,
    current_user: CurrentUser,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 100,
):
    service = BankAccountService(BankAccountRepository(db))
    return service.list_accounts(current_user.id, skip=skip, limit=limit)


@router.get(
    "/{account_id}",
    response_model=BankAccountResponse,
    summary="Get bank account by id",
)
def get_bank_account(account_id: int, db: DbDep, current_user: CurrentUser):
    service = BankAccountService(BankAccountRepository(db))
    return service.get_account(account_id, current_user.id)


# Endpoint untuk membuat rekening bank baru
@router.post(
    "",
    response_model=BankAccountResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create bank account",
)
def create_bank_account(
    request: BankAccountCreate,
    db: DbDep,
    current_user: CurrentUser,
):
    service = BankAccountService(BankAccountRepository(db))

    return service.create_account(
        account_number=request.account_number,
        account_name=request.account_name,
        bank_name=request.bank_name,
        balance=request.balance,
        user_id=current_user.id,
    )
    
    
# Endpoint untuk memperbarui rekening bank yang sudah ada
@router.put(
    "/{account_id}",
    response_model=BankAccountResponse,
    summary="Update bank account",
)
def update_bank_account(
    account_id: int,
    request: BankAccountUpdate,
    db: DbDep,
    current_user: CurrentUser,
):
    service = BankAccountService(BankAccountRepository(db))

    return service.update_account(
        account_id=account_id,
        user_id=current_user.id,
        account_name=request.account_name,
        bank_name=request.bank_name,
        balance=request.balance,
    )


# Endpoint untuk menghapus rekening bank dari database
@router.delete(
    "/{account_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete bank account",
)
def delete_bank_account(
    account_id: int,
    db: DbDep,
    current_user: CurrentUser,
):
    service = BankAccountService(BankAccountRepository(db))
    service.delete_account(account_id, current_user.id)
