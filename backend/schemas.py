from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    updated_at: datetime

class PortfolioCreate(BaseModel):
    user_id: int

class PortfolioResponse(BaseModel):
    id: int
    user_id: int
    total_value: float
    created_at: datetime
    updated_at: datetime

class HoldingCreate(BaseModel):
    portfolio_id: int
    symbol: str
    quantity: float
    purchase_price: float

class HoldingResponse(BaseModel):
    id: int
    portfolio_id: int
    symbol: str
    quantity: float
    purchase_price: float
    created_at: datetime
    updated_at: datetime
