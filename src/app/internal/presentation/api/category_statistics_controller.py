from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from typing import List
from src.config.database import get_db
from src.app.internal.data.repositories.category_statistics_repository import CategoryStatisticsRepository
from src.app.internal.domain.entities.category_statistics_entity import CategoryStatisticsEntity
from src.app.internal.presentation.scheme.category_statistics_schema import (
    CategoryStatisticsCreate,
    CategoryStatisticsUpdate,
    CategoryStatisticsResponse
)

router = APIRouter(prefix="/category-statistics", tags=["category-statistics"])


def get_category_statistics_repository(db: Session = Depends(get_db)):
    return CategoryStatisticsRepository(db)


@router.post("/", response_model=CategoryStatisticsResponse)
async def create_category_statistics(
    category_statistics: CategoryStatisticsCreate,
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    statistics_data = category_statistics.dict()
    statistics_data['id'] = str(uuid4())
    statistics_entity = CategoryStatisticsEntity(**statistics_data)
    created_statistics = await category_statistics_repo.create_category_statistics(statistics_entity)
    return created_statistics


@router.get("/{statistics_id}", response_model=CategoryStatisticsResponse)
async def get_category_statistics(
    statistics_id: UUID,
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    statistics = await category_statistics_repo.get_category_statistics(statistics_id)
    if statistics is None:
        raise HTTPException(status_code=404, detail="Category statistics not found")
    return statistics


@router.get("/", response_model=List[CategoryStatisticsResponse])
async def get_all_category_statistics(
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    return await category_statistics_repo.get_all_category_statistics()


@router.get("/user/{user_id}", response_model=List[CategoryStatisticsResponse])
async def get_category_statistics_by_user(
    user_id: UUID,
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    return await category_statistics_repo.get_category_statistics_by_user(user_id)


@router.get("/user/{user_id}/category/{category}", response_model=List[CategoryStatisticsResponse])
async def get_category_statistics_by_user_and_category(
    user_id: UUID,
    category: str,
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    return await category_statistics_repo.get_category_statistics_by_user_and_category(user_id, category)


@router.put("/{statistics_id}", response_model=CategoryStatisticsResponse)
async def update_category_statistics(
    statistics_id: UUID,
    statistics_update: CategoryStatisticsUpdate,
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    existing_statistics = await category_statistics_repo.get_category_statistics(statistics_id)
    if existing_statistics is None:
        raise HTTPException(status_code=404, detail="Category statistics not found")

    update_data = statistics_update.dict(exclude_unset=True)
    updated_statistics_data = existing_statistics.dict()
    updated_statistics_data.update(update_data)

    updated_statistics_entity = CategoryStatisticsEntity(**updated_statistics_data)
    updated_statistics = await category_statistics_repo.update_category_statistics(statistics_id, updated_statistics_entity)

    if updated_statistics is None:
        raise HTTPException(status_code=404, detail="Category statistics not found")

    return updated_statistics


@router.delete("/{statistics_id}")
async def delete_category_statistics(
    statistics_id: UUID,
    category_statistics_repo: CategoryStatisticsRepository = Depends(get_category_statistics_repository)
):
    success = await category_statistics_repo.delete_category_statistics(statistics_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category statistics not found")
    return {"message": "Category statistics deleted successfully"}