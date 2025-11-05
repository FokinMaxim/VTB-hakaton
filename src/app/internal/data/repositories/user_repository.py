from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from src.app.internal.data.models.user_model import UserModel
from src.app.internal.domain.entities.user_entity import UserEntity
from src.app.internal.domain.interfaces.user_interface import IUserRepository


class UserRepository(IUserRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create_user(self, user: UserEntity) -> UserEntity:
        db_user = UserModel(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserEntity.from_orm(db_user)

    async def get_user(self, user_uuid: UUID) -> Optional[UserEntity]:
        db_user = self.db.query(UserModel).filter(UserModel.uuid == user_uuid).first()
        if db_user:
            return UserEntity.from_orm(db_user)
        return None

    async def get_all_users(self) -> List[UserEntity]:
        db_users = self.db.query(UserModel).all()
        return [UserEntity.from_orm(user) for user in db_users]

    async def update_user(self, user_uuid: UUID, user: UserEntity) -> Optional[UserEntity]:
        db_user = self.db.query(UserModel).filter(UserModel.uuid == user_uuid).first()
        if db_user:
            for key, value in user.dict().items():
                setattr(db_user, key, value)
            self.db.commit()
            self.db.refresh(db_user)
            return UserEntity.from_orm(db_user)
        return None

    async def delete_user(self, user_uuid: UUID) -> bool:
        db_user = self.db.query(UserModel).filter(UserModel.uuid == user_uuid).first()
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False