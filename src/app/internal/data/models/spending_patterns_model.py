from sqlalchemy import Column, String, DECIMAL, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base
import uuid


class SpendingPatternsModel(Base):
    __tablename__ = "облачные_паттерны_трат"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    pattern_type = Column(String, nullable=False)
    category = Column(String, nullable=False)
    average_sum = Column(DECIMAL(10, 2), nullable=False)
    average_week_consumption = Column(DECIMAL(5, 2), nullable=False)
    week_day = Column(String, nullable=False)
    time_of_day = Column(String, nullable=False)
