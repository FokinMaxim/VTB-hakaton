from pydantic import BaseModel
from uuid import UUID
from datetime import date


class UserCreate(BaseModel):
    region: str
    age_group: str
    income_group: str
    register_date: date
    is_active: bool


class UserUpdate(BaseModel):
    region: str | None = None
    age_group: str | None = None
    income_group: str | None = None
    register_date: date | None = None
    is_active: bool | None = None


class UserResponse(BaseModel):
    uuid: UUID
    region: str
    age_group: str
    income_group: str
    register_date: date
    is_active: bool

    class Config:
        from_attributes = True