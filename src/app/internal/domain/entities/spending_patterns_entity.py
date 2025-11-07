from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class SpendingPatternsEntity(BaseModel):
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