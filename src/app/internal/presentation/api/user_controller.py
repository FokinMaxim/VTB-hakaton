from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID, uuid4
from typing import List
from src.config.database import get_db
from src.app.internal.data.repositories.user_repository import UserRepository
from src.app.internal.domain.entities.user_entity import UserEntity
from src.app.internal.presentation.scheme.user_schema import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])


def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)


@router.post("/", response_model=UserResponse)
async def create_user(
        user: UserCreate,
        user_repo: UserRepository = Depends(get_user_repository)
):
    user_data = user.dict()
    user_data['uuid'] = str(uuid4())
    user_entity = UserEntity(**user_data)
    created_user = await user_repo.create_user(user_entity)
    return created_user


@router.get("/{user_uuid}", response_model=UserResponse)
async def get_user(
        user_uuid: UUID,
        user_repo: UserRepository = Depends(get_user_repository)
):
    user = await user_repo.get_user(user_uuid)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[UserResponse])
async def get_all_users(user_repo: UserRepository = Depends(get_user_repository)):
    return await user_repo.get_all_users()


@router.put("/{user_uuid}", response_model=UserResponse)
async def update_user(
        user_uuid: UUID,
        user_update: UserUpdate,
        user_repo: UserRepository = Depends(get_user_repository)
):
    existing_user = await user_repo.get_user(user_uuid)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_update.dict(exclude_unset=True)
    updated_user_data = existing_user.dict()
    updated_user_data.update(update_data)

    updated_user_entity = UserEntity(**updated_user_data)
    updated_user = await user_repo.update_user(user_uuid, updated_user_entity)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@router.delete("/{user_uuid}")
async def delete_user(
        user_uuid: UUID,
        user_repo: UserRepository = Depends(get_user_repository)
):
    success = await user_repo.delete_user(user_uuid)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}