from sqlalchemy import Column, String, Integer, Date, DECIMAL
from sqlalchemy.dialects.postgresql import UUID
from src.config.database import Base
import uuid

class MarketTrendsModel(Base):
    __tablename__ = "облачные_рыночные_тренды"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category = Column(String, nullable=False)
    region = Column(String, nullable=False)
    age_group = Column(String, nullable=False)
    average_income = Column(DECIMAL(10, 2), nullable=False)
    user_amount = Column(Integer, nullable=False)
    difference_from_previous_month = Column(DECIMAL(5, 2), nullable=False)
    collection_date = Column(Date, nullable=False)