from pydantic import BaseModel
from uuid import UUID
from datetime import date
from decimal import Decimal


class OfferEntity(BaseModel):
    id: UUID
    title: str
    description: str
    partner: str
    cashback_percent: Decimal
    valid_from: date
    valid_to: date
    active: bool

    class Config:
        from_attributes = True