from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from typing import List, Optional
from src.config.database import get_db
from src.app.internal.data.repositories.market_trends_repository import MarketTrendsRepository
from src.app.internal.domain.entities.market_trends_entity import MarketTrendsEntity
from src.app.internal.presentation.scheme.market_trends_schema import (
    MarketTrendsCreate,
    MarketTrendsUpdate,
    MarketTrendsResponse
)

router = APIRouter(prefix="/market-trends", tags=["market-trends"])


def get_market_trends_repository(db: Session = Depends(get_db)):
    return MarketTrendsRepository(db)


@router.post("/", response_model=MarketTrendsResponse)
async def create_market_trend(
    trend: MarketTrendsCreate,
    market_trends_repo: MarketTrendsRepository = Depends(get_market_trends_repository)
):
    trend_data = trend.dict()
    trend_data['id'] = str(uuid4())
    trend_entity = MarketTrendsEntity(**trend_data)
    created_trend = await market_trends_repo.create_market_trend(trend_entity)
    return created_trend


@router.get("/{trend_id}", response_model=MarketTrendsResponse)
async def get_market_trend(
    trend_id: UUID,
    market_trends_repo: MarketTrendsRepository = Depends(get_market_trends_repository)
):
    trend = await market_trends_repo.get_market_trend(trend_id)
    if trend is None:
        raise HTTPException(status_code=404, detail="Market trend not found")
    return trend


@router.get("/", response_model=List[MarketTrendsResponse])
async def get_market_trends(
    category: Optional[str] = Query(None, description="Filter by category"),
    region: Optional[str] = Query(None, description="Filter by region"),
    age_group: Optional[str] = Query(None, description="Filter by age group"),
    market_trends_repo: MarketTrendsRepository = Depends(get_market_trends_repository)
):
    if category or region or age_group:
        return await market_trends_repo.get_market_trends_by_filters(
            category=category,
            region=region,
            age_group=age_group
        )
    else:
        return await market_trends_repo.get_all_market_trends()


@router.put("/{trend_id}", response_model=MarketTrendsResponse)
async def update_market_trend(
    trend_id: UUID,
    trend_update: MarketTrendsUpdate,
    market_trends_repo: MarketTrendsRepository = Depends(get_market_trends_repository)
):
    existing_trend = await market_trends_repo.get_market_trend(trend_id)
    if existing_trend is None:
        raise HTTPException(status_code=404, detail="Market trend not found")

    update_data = trend_update.dict(exclude_unset=True)
    updated_trend_data = existing_trend.dict()
    updated_trend_data.update(update_data)

    updated_trend_entity = MarketTrendsEntity(**updated_trend_data)
    updated_trend = await market_trends_repo.update_market_trend(trend_id, updated_trend_entity)

    if updated_trend is None:
        raise HTTPException(status_code=404, detail="Market trend not found")

    return updated_trend


@router.delete("/{trend_id}")
async def delete_market_trend(
    trend_id: UUID,
    market_trends_repo: MarketTrendsRepository = Depends(get_market_trends_repository)
):
    success = await market_trends_repo.delete_market_trend(trend_id)
    if not success:
        raise HTTPException(status_code=404, detail="Market trend not found")
    return {"message": "Market trend deleted successfully"}