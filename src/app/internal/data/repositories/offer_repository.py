from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from src.app.internal.data.models.offer_model import OfferModel
from src.app.internal.domain.entities.offer_entity import OfferEntity
from src.app.internal.domain.interfaces.offer_interface import IOfferRepository


class OfferRepository(IOfferRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create_offer(self, offer: OfferEntity) -> OfferEntity:
        db_offer = OfferModel(**offer.dict())
        self.db.add(db_offer)
        self.db.commit()
        self.db.refresh(db_offer)
        return OfferEntity.from_orm(db_offer)

    async def get_offer(self, offer_id: UUID) -> Optional[OfferEntity]:
        db_offer = self.db.query(OfferModel).filter(OfferModel.id == offer_id).first()
        if db_offer:
            return OfferEntity.from_orm(db_offer)
        return None

    async def get_all_offers(self) -> List[OfferEntity]:
        db_offers = self.db.query(OfferModel).all()
        return [OfferEntity.from_orm(offer) for offer in db_offers]

    async def update_offer(self, offer_id: UUID, offer: OfferEntity) -> Optional[OfferEntity]:
        db_offer = self.db.query(OfferModel).filter(OfferModel.id == offer_id).first()
        if db_offer:
            for key, value in offer.dict().items():
                setattr(db_offer, key, value)
            self.db.commit()
            self.db.refresh(db_offer)
            return OfferEntity.from_orm(db_offer)
        return None

    async def delete_offer(self, offer_id: UUID) -> bool:
        db_offer = self.db.query(OfferModel).filter(OfferModel.id == offer_id).first()
        if db_offer:
            self.db.delete(db_offer)
            self.db.commit()
            return True
        return False

    async def get_active_offers(self) -> List[OfferEntity]:
        from datetime import date
        db_offers = self.db.query(OfferModel).filter(
            OfferModel.active == True,
            OfferModel.valid_from <= date.today(),
            OfferModel.valid_to >= date.today()
        ).all()
        return [OfferEntity.from_orm(offer) for offer in db_offers]