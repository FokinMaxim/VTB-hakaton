from sqlalchemy import Column, String, Boolean, Date, DECIMAL
from sqlalchemy.dialects.postgresql import UUID
from src.config.database import Base
import uuid


class OfferModel(Base):
    __tablename__ = "offers"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    partner = Column(String, nullable=False)
    cashback_percent = Column(DECIMAL(5, 2), nullable=False)
    valid_from = Column(Date, nullable=False)
    valid_to = Column(Date, nullable=False)
    active = Column(Boolean, nullable=False, default=True)