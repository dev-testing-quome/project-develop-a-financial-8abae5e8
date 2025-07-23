from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class UserRead(BaseModel):
    id: int
    username: str
    email: str
    kyc_verified: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class PortfolioCreate(BaseModel):
    user_id: int

class PortfolioRead(BaseModel):
    id: int
    user_id: int
    total_value: Optional[int] = 0
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    portfolio_id: int
    symbol: str
    quantity: int
    price: float
    transaction_type: str

class TransactionRead(BaseModel):
    id: int
    portfolio_id: int
    symbol: str
    quantity: int
    price: float
    transaction_type: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True
