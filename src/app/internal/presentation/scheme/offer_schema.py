from pydantic import BaseModel
from uuid import UUID
from datetime import date
from decimal import Decimal
from typing import Optional


class OfferCreate(BaseModel):
    title: str
    description: str
    partner: str
    cashback_percent: Decimal
    valid_from: date
    valid_to: date
    active: bool = True


class OfferUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    partner: Optional[str] = None
    cashback_percent: Optional[Decimal] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None
    active: Optional[bool] = None


class OfferResponse(BaseModel):
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