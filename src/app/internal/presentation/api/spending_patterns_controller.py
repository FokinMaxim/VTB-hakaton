from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from typing import List
from src.config.database import get_db
from src.app.internal.data.repositories.spending_patterns_repository import SpendingPatternsRepository
from src.app.internal.domain.entities.spending_patterns_entity import SpendingPatternsEntity
from src.app.internal.presentation.scheme.spending_patterns_schema import (
    SpendingPatternsCreate,
    SpendingPatternsUpdate,
    SpendingPatternsResponse
)

router = APIRouter(prefix="/spending-patterns", tags=["spending-patterns"])


def get_spending_patterns_repository(db: Session = Depends(get_db)):
    return SpendingPatternsRepository(db)


@router.post("/", response_model=SpendingPatternsResponse)
async def create_spending_pattern(
    spending_pattern: SpendingPatternsCreate,
    spending_patterns_repo: SpendingPatternsRepository = Depends(get_spending_patterns_repository)
):
    pattern_data = spending_pattern.dict()
    pattern_data['id'] = str(uuid4())
    pattern_entity = SpendingPatternsEntity(**pattern_data)
    created_pattern = await spending_patterns_repo.create_spending_pattern(pattern_entity)
    return created_pattern


@router.get("/{pattern_id}", response_model=SpendingPatternsResponse)
async def get_spending_pattern(
    pattern_id: UUID,
    spending_patterns_repo: SpendingPatternsRepository = Depends(get_spending_patterns_repository)
):
    pattern = await spending_patterns_repo.get_spending_pattern(pattern_id)
    if pattern is None:
        raise HTTPException(status_code=404, detail="Spending pattern not found")
    return pattern


@router.get("/", response_model=List[SpendingPatternsResponse])
async def get_all_spending_patterns(
    spending_patterns_repo: SpendingPatternsRepository = Depends(get_spending_patterns_repository)
):
    return await spending_patterns_repo.get_all_spending_patterns()


@router.get("/user/{user_id}", response_model=List[SpendingPatternsResponse])
async def get_spending_patterns_by_user(
    user_id: UUID,
    spending_patterns_repo: SpendingPatternsRepository = Depends(get_spending_patterns_repository)
):
    return await spending_patterns_repo.get_spending_patterns_by_user(user_id)


@router.put("/{pattern_id}", response_model=SpendingPatternsResponse)
async def update_spending_pattern(
    pattern_id: UUID,
    pattern_update: SpendingPatternsUpdate,
    spending_patterns_repo: SpendingPatternsRepository = Depends(get_spending_patterns_repository)
):
    existing_pattern = await spending_patterns_repo.get_spending_pattern(pattern_id)
    if existing_pattern is None:
        raise HTTPException(status_code=404, detail="Spending pattern not found")

    update_data = pattern_update.dict(exclude_unset=True)
    updated_pattern_data = existing_pattern.dict()
    updated_pattern_data.update(update_data)

    updated_pattern_entity = SpendingPatternsEntity(**updated_pattern_data)
    updated_pattern = await spending_patterns_repo.update_spending_pattern(pattern_id, updated_pattern_entity)

    if updated_pattern is None:
        raise HTTPException(status_code=404, detail="Spending pattern not found")

    return updated_pattern


@router.delete("/{pattern_id}")
async def delete_spending_pattern(
    pattern_id: UUID,
    spending_patterns_repo: SpendingPatternsRepository = Depends(get_spending_patterns_repository)
):
    success = await spending_patterns_repo.delete_spending_pattern(pattern_id)
    if not success:
        raise HTTPException(status_code=404, detail="Spending pattern not found")
    return {"message": "Spending pattern deleted successfully"}