from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import date
from typing import Optional


class MarketTrendsCreate(BaseModel):
    category: str
    region: str
    age_group: str
    average_income: Decimal
    user_amount: int
    difference_from_previous_month: Decimal
    collection_date: date


class MarketTrendsUpdate(BaseModel):
    category: Optional[str] = None
    region: Optional[str] = None
    age_group: Optional[str] = None
    average_income: Optional[Decimal] = None
    user_amount: Optional[int] = None
    difference_from_previous_month: Optional[Decimal] = None
    collection_date: Optional[date] = None


class MarketTrendsResponse(BaseModel):
    id: UUID
    category: str
    region: str
    age_group: str
    average_income: Decimal
    user_amount: int
    difference_from_previous_month: Decimal
    collection_date: date

    class Config:
        from_attributes = True