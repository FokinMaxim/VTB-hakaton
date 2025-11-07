from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import date


class CategoryStatisticsEntity(BaseModel):
    id: UUID
    user_id: UUID
    category: str
    avarage_consumption: Decimal
    total_consumption: Decimal
    transaction_ammount: int
    frequency_spending: Decimal
    time_period: str
    statistics_date: date

    class Config:
        from_attributes = True