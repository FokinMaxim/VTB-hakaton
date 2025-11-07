from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from datetime import date


class CategoryStatisticsCreate(BaseModel):
    user_id: UUID
    category: str
    avarage_consumption: Decimal
    total_consumption: Decimal
    transaction_ammount: int
    frequency_spending: Decimal
    time_period: str
    statistics_date: date


class CategoryStatisticsUpdate(BaseModel):
    user_id: UUID | None = None
    category: str | None = None
    avarage_consumption: Decimal | None = None
    total_consumption: Decimal | None = None
    transaction_ammount: int | None = None
    frequency_spending: Decimal | None = None
    time_period: str | None = None
    statistics_date: date | None = None


class CategoryStatisticsResponse(BaseModel):
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