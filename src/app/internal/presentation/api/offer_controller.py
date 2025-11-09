from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from typing import List
from src.config.database import get_db
from src.app.internal.data.repositories.offer_repository import OfferRepository
from src.app.internal.domain.entities.offer_entity import OfferEntity
from src.app.internal.presentation.scheme.offer_schema import OfferCreate, OfferUpdate, OfferResponse

router = APIRouter(prefix="/offers", tags=["offers"])


def get_offer_repository(db: Session = Depends(get_db)):
    return OfferRepository(db)


@router.post("/", response_model=OfferResponse)
async def create_offer(
    offer: OfferCreate,
    offer_repo: OfferRepository = Depends(get_offer_repository)
):
    offer_data = offer.dict()
    offer_data['id'] = uuid4()
    offer_entity = OfferEntity(**offer_data)
    created_offer = await offer_repo.create_offer(offer_entity)
    return created_offer


@router.get("/", response_model=List[OfferResponse])
async def get_all_offers(offer_repo: OfferRepository = Depends(get_offer_repository)):
    return await offer_repo.get_all_offers()


@router.get("/active", response_model=List[OfferResponse])
async def get_active_offers(offer_repo: OfferRepository = Depends(get_offer_repository)):
    return await offer_repo.get_active_offers()


@router.get("/{offer_id}", response_model=OfferResponse)
async def get_offer(
    offer_id: UUID,
    offer_repo: OfferRepository = Depends(get_offer_repository)
):
    offer = await offer_repo.get_offer(offer_id)
    if offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer


@router.put("/{offer_id}", response_model=OfferResponse)
async def update_offer(
    offer_id: UUID,
    offer_update: OfferUpdate,
    offer_repo: OfferRepository = Depends(get_offer_repository)
):
    existing_offer = await offer_repo.get_offer(offer_id)
    if existing_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")

    update_data = offer_update.dict(exclude_unset=True)
    updated_offer_data = existing_offer.dict()
    updated_offer_data.update(update_data)

    updated_offer_entity = OfferEntity(**updated_offer_data)
    updated_offer = await offer_repo.update_offer(offer_id, updated_offer_entity)

    if updated_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")

    return updated_offer


@router.delete("/{offer_id}")
async def delete_offer(
    offer_id: UUID,
    offer_repo: OfferRepository = Depends(get_offer_repository)
):
    success = await offer_repo.delete_offer(offer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Offer not found")
    return {"message": "Offer deleted successfully"}