from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from src.app.internal.domain.entities.offer_entity import OfferEntity


class IOfferRepository(ABC):

    @abstractmethod
    async def create_offer(self, offer: OfferEntity) -> OfferEntity:
        pass

    @abstractmethod
    async def get_offer(self, offer_id: UUID) -> Optional[OfferEntity]:
        pass

    @abstractmethod
    async def get_all_offers(self) -> List[OfferEntity]:
        pass

    @abstractmethod
    async def update_offer(self, offer_id: UUID, offer: OfferEntity) -> Optional[OfferEntity]:
        pass

    @abstractmethod
    async def delete_offer(self, offer_id: UUID) -> bool:
        pass

    @abstractmethod
    async def get_active_offers(self) -> List[OfferEntity]:
        pass