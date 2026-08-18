from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


# Attribut data yang diperlukan untuk create bank account  
class BankAccountCreate(BaseModel):
    account_number: str
    account_name: str
    bank_name: str
    balance: Decimal = Field(default=Decimal("0.00"), ge=0)

# Attribut data yang diperlukan untuk update bank accout
class BankAccountUpdate(BaseModel):
    account_name: str
    bank_name: str
    balance: Decimal = Field(ge=0)

# Attribut data yang dikembalikan saat melakukan create, update, dan get bank account
class BankAccountResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    account_number: str
    account_name: str
    bank_name: str
    balance: Decimal
    user_id: int
    created_at: datetime
    updated_at: datetime
