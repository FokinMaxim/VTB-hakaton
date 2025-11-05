from fastapi import FastAPI
from src.config.database import engine, Base
from src.app.internal.presentation.api.user_controller import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users API",
    description="CRUD API for Users management",
)

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Users API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}