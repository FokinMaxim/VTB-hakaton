from sqlalchemy import Column, String, Integer, DECIMAL, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from src.config.database import Base
import uuid


class CategoryStatisticsModel(Base):
    __tablename__ = "облачные_статистика_категорий"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    category = Column(String, nullable=False)
    avarage_consumption = Column(DECIMAL(10, 2), nullable=False)
    total_consumption = Column(DECIMAL(12, 2), nullable=False)
    transaction_ammount = Column(Integer, nullable=False)
    frequency_spending = Column(DECIMAL(5, 2), nullable=False)
    time_period = Column(String, nullable=False)
    statistics_date = Column(Date, nullable=False)
