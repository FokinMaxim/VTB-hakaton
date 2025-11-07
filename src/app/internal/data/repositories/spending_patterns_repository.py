from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from src.app.internal.data.models.spending_patterns_model import SpendingPatternsModel
from src.app.internal.domain.entities.spending_patterns_entity import SpendingPatternsEntity
from src.app.internal.domain.interfaces.spending_patterns_interface import ISpendingPatternsRepository


class SpendingPatternsRepository(ISpendingPatternsRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create_spending_pattern(self, spending_pattern: SpendingPatternsEntity) -> SpendingPatternsEntity:
        db_spending_pattern = SpendingPatternsModel(**spending_pattern.dict())
        self.db.add(db_spending_pattern)
        self.db.commit()
        self.db.refresh(db_spending_pattern)
        return SpendingPatternsEntity.from_orm(db_spending_pattern)

    async def get_spending_pattern(self, pattern_id: UUID) -> Optional[SpendingPatternsEntity]:
        db_pattern = self.db.query(SpendingPatternsModel).filter(SpendingPatternsModel.id == pattern_id).first()
        if db_pattern:
            return SpendingPatternsEntity.from_orm(db_pattern)
        return None

    async def get_all_spending_patterns(self) -> List[SpendingPatternsEntity]:
        db_patterns = self.db.query(SpendingPatternsModel).all()
        return [SpendingPatternsEntity.from_orm(pattern) for pattern in db_patterns]

    async def get_spending_patterns_by_user(self, user_id: UUID) -> List[SpendingPatternsEntity]:
        db_patterns = self.db.query(SpendingPatternsModel).filter(SpendingPatternsModel.user_id == user_id).all()
        return [SpendingPatternsEntity.from_orm(pattern) for pattern in db_patterns]

    async def update_spending_pattern(self, pattern_id: UUID, spending_pattern: SpendingPatternsEntity) -> Optional[SpendingPatternsEntity]:
        db_pattern = self.db.query(SpendingPatternsModel).filter(SpendingPatternsModel.id == pattern_id).first()
        if db_pattern:
            for key, value in spending_pattern.dict().items():
                setattr(db_pattern, key, value)
            self.db.commit()
            self.db.refresh(db_pattern)
            return SpendingPatternsEntity.from_orm(db_pattern)
        return None

    async def delete_spending_pattern(self, pattern_id: UUID) -> bool:
        db_pattern = self.db.query(SpendingPatternsModel).filter(SpendingPatternsModel.id == pattern_id).first()
        if db_pattern:
            self.db.delete(db_pattern)
            self.db.commit()
            return True
        return False