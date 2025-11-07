from fastapi import FastAPI
from src.config.database import engine, Base
from src.app.internal.presentation.api.user_controller import router as user_router
from src.app.internal.presentation.api.spending_patterns_controller import router as spending_patterns_router
from src.app.internal.presentation.api.category_statistics_controller import router as category_statistics_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users API",
    description="CRUD API for Users management",
)

app.include_router(user_router)
app.include_router(spending_patterns_router)
app.include_router(category_statistics_router)


@app.get("/")
async def root():
    return {"message": "Users API is running"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}