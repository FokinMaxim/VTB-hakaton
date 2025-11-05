from pydantic import BaseModel
from uuid import UUID
from datetime import date


class UserEntity(BaseModel):
    uuid: UUID
    region: str
    age_group: str
    income_group: str
    register_date: date
    is_active: bool

    class Config:
        from_attributes = True