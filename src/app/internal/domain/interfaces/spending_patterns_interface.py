from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from src.app.internal.domain.entities.spending_patterns_entity import SpendingPatternsEntity


class ISpendingPatternsRepository(ABC):

    @abstractmethod
    async def create_spending_pattern(self, spending_pattern: SpendingPatternsEntity) -> SpendingPatternsEntity:
        pass

    @abstractmethod
    async def get_spending_pattern(self, pattern_id: UUID) -> Optional[SpendingPatternsEntity]:
        pass

    @abstractmethod
    async def get_all_spending_patterns(self) -> List[SpendingPatternsEntity]:
        pass

    @abstractmethod
    async def get_spending_patterns_by_user(self, user_id: UUID) -> List[SpendingPatternsEntity]:
        pass

    @abstractmethod
    async def update_spending_pattern(self, pattern_id: UUID, spending_pattern: SpendingPatternsEntity) -> Optional[SpendingPatternsEntity]:
        pass

    @abstractmethod
    async def delete_spending_pattern(self, pattern_id: UUID) -> bool:
        pass