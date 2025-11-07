from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from src.app.internal.domain.entities.category_statistics_entity import CategoryStatisticsEntity


class ICategoryStatisticsRepository(ABC):

    @abstractmethod
    async def create_category_statistics(self, category_statistics: CategoryStatisticsEntity) -> CategoryStatisticsEntity:
        pass

    @abstractmethod
    async def get_category_statistics(self, statistics_id: UUID) -> Optional[CategoryStatisticsEntity]:
        pass

    @abstractmethod
    async def get_all_category_statistics(self) -> List[CategoryStatisticsEntity]:
        pass

    @abstractmethod
    async def get_category_statistics_by_user(self, user_id: UUID) -> List[CategoryStatisticsEntity]:
        pass

    @abstractmethod
    async def get_category_statistics_by_user_and_category(self, user_id: UUID, category: str) -> List[CategoryStatisticsEntity]:
        pass

    @abstractmethod
    async def update_category_statistics(self, statistics_id: UUID, category_statistics: CategoryStatisticsEntity) -> Optional[CategoryStatisticsEntity]:
        pass

    @abstractmethod
    async def delete_category_statistics(self, statistics_id: UUID) -> bool:
        pass