from sqlalchemy import Column, String, Boolean, Date
from sqlalchemy.dialects.postgresql import UUID
from src.config.database import Base
import uuid


class UserModel(Base):
    __tablename__ = "users"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    region = Column(String, nullable=False)
    age_group = Column(String, nullable=False)
    income_group = Column(String, nullable=False)
    register_date = Column(Date, nullable=False)
    is_active = Column(Boolean, nullable=False)