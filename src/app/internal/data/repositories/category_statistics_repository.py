from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from src.app.internal.data.models.category_statistics_model import CategoryStatisticsModel
from src.app.internal.domain.entities.category_statistics_entity import CategoryStatisticsEntity
from src.app.internal.domain.interfaces.category_statistics_interface import ICategoryStatisticsRepository


class CategoryStatisticsRepository(ICategoryStatisticsRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create_category_statistics(self, category_statistics: CategoryStatisticsEntity) -> CategoryStatisticsEntity:
        db_category_statistics = CategoryStatisticsModel(**category_statistics.dict())
        self.db.add(db_category_statistics)
        self.db.commit()
        self.db.refresh(db_category_statistics)
        return CategoryStatisticsEntity.from_orm(db_category_statistics)

    async def get_category_statistics(self, statistics_id: UUID) -> Optional[CategoryStatisticsEntity]:
        db_statistics = self.db.query(CategoryStatisticsModel).filter(CategoryStatisticsModel.id == statistics_id).first()
        if db_statistics:
            return CategoryStatisticsEntity.from_orm(db_statistics)
        return None

    async def get_all_category_statistics(self) -> List[CategoryStatisticsEntity]:
        db_statistics = self.db.query(CategoryStatisticsModel).all()
        return [CategoryStatisticsEntity.from_orm(statistics) for statistics in db_statistics]

    async def get_category_statistics_by_user(self, user_id: UUID) -> List[CategoryStatisticsEntity]:
        db_statistics = self.db.query(CategoryStatisticsModel).filter(CategoryStatisticsModel.user_id == user_id).all()
        return [CategoryStatisticsEntity.from_orm(statistics) for statistics in db_statistics]

    async def get_category_statistics_by_user_and_category(self, user_id: UUID, category: str) -> List[CategoryStatisticsEntity]:
        db_statistics = self.db.query(CategoryStatisticsModel).filter(
            CategoryStatisticsModel.user_id == user_id,
            CategoryStatisticsModel.category == category
        ).all()
        return [CategoryStatisticsEntity.from_orm(statistics) for statistics in db_statistics]

    async def update_category_statistics(self, statistics_id: UUID, category_statistics: CategoryStatisticsEntity) -> Optional[CategoryStatisticsEntity]:
        db_statistics = self.db.query(CategoryStatisticsModel).filter(CategoryStatisticsModel.id == statistics_id).first()
        if db_statistics:
            for key, value in category_statistics.dict().items():
                setattr(db_statistics, key, value)
            self.db.commit()
            self.db.refresh(db_statistics)
            return CategoryStatisticsEntity.from_orm(db_statistics)
        return None

    async def delete_category_statistics(self, statistics_id: UUID) -> bool:
        db_statistics = self.db.query(CategoryStatisticsModel).filter(CategoryStatisticsModel.id == statistics_id).first()
        if db_statistics:
            self.db.delete(db_statistics)
            self.db.commit()
            return True
        return False