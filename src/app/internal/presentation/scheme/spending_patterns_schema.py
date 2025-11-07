from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class SpendingPatternsCreate(BaseModel):
    user_id: UUID
    pattern_type: str
    category: str
    average_sum: Decimal
    average_week_consumption: Decimal
    week_day: str
    time_of_day: str


class SpendingPatternsUpdate(BaseModel):
    user_id: UUID | None = None
    pattern_type: str | None = None
    category: str | None = None
    average_sum: Decimal | None = None
    average_week_consumption: Decimal | None = None
    week_day: str | None = None
    time_of_day: str | None = None


class SpendingPatternsResponse(BaseModel):
    id: UUID
    user_id: UUID
    pattern_type: str
    category: str
    average_sum: Decimal
    average_week_consumption: Decimal
    week_day: str
    time_of_day: str

    class Config:
        from_attributes = True