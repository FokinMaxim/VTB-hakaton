from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import date

class MarketTrendsEntity(BaseModel):
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