from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from src.app.internal.domain.entities.market_trends_entity import MarketTrendsEntity

class IMarketTrendsRepository(ABC):

    @abstractmethod
    async def create_market_trend(self, trend: MarketTrendsEntity) -> MarketTrendsEntity:
        pass

    @abstractmethod
    async def get_market_trend(self, trend_id: UUID) -> Optional[MarketTrendsEntity]:
        pass

    @abstractmethod
    async def get_market_trends_by_filters(self, category: Optional[str] = None,
                                         region: Optional[str] = None,
                                         age_group: Optional[str] = None) -> List[MarketTrendsEntity]:
        pass

    @abstractmethod
    async def get_all_market_trends(self) -> List[MarketTrendsEntity]:
        pass

    @abstractmethod
    async def update_market_trend(self, trend_id: UUID, trend: MarketTrendsEntity) -> Optional[MarketTrendsEntity]:
        pass

    @abstractmethod
    async def delete_market_trend(self, trend_id: UUID) -> bool:
        pass