from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from src.app.internal.data.models.market_trends_model import MarketTrendsModel
from src.app.internal.domain.entities.market_trends_entity import MarketTrendsEntity
from src.app.internal.domain.interfaces.market_trends_interface import IMarketTrendsRepository


class MarketTrendsRepository(IMarketTrendsRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create_market_trend(self, trend: MarketTrendsEntity) -> MarketTrendsEntity:
        db_trend = MarketTrendsModel(**trend.dict())
        self.db.add(db_trend)
        self.db.commit()
        self.db.refresh(db_trend)
        return MarketTrendsEntity.from_orm(db_trend)

    async def get_market_trend(self, trend_id: UUID) -> Optional[MarketTrendsEntity]:
        db_trend = self.db.query(MarketTrendsModel).filter(MarketTrendsModel.id == trend_id).first()
        if db_trend:
            return MarketTrendsEntity.from_orm(db_trend)
        return None

    async def get_market_trends_by_filters(self, category: Optional[str] = None,
                                           region: Optional[str] = None,
                                           age_group: Optional[str] = None) -> List[MarketTrendsEntity]:
        query = self.db.query(MarketTrendsModel)

        if category:
            query = query.filter(MarketTrendsModel.category == category)
        if region:
            query = query.filter(MarketTrendsModel.region == region)
        if age_group:
            query = query.filter(MarketTrendsModel.age_group == age_group)

        db_trends = query.all()
        return [MarketTrendsEntity.from_orm(trend) for trend in db_trends]

    async def get_all_market_trends(self) -> List[MarketTrendsEntity]:
        db_trends = self.db.query(MarketTrendsModel).all()
        return [MarketTrendsEntity.from_orm(trend) for trend in db_trends]

    async def update_market_trend(self, trend_id: UUID, trend: MarketTrendsEntity) -> Optional[
        MarketTrendsEntity]:
        db_trend = self.db.query(MarketTrendsModel).filter(MarketTrendsModel.id == trend_id).first()
        if db_trend:
            for key, value in trend.dict().items():
                setattr(db_trend, key, value)
            self.db.commit()
            self.db.refresh(db_trend)
            return MarketTrendsEntity.from_orm(db_trend)
        return None

    async def delete_market_trend(self, trend_id: UUID) -> bool:
        db_trend = self.db.query(MarketTrendsModel).filter(MarketTrendsModel.id == trend_id).first()
        if db_trend:
            self.db.delete(db_trend)
            self.db.commit()
            return True
        return False