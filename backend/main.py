from fastapi import FastAPI

from backend.api.routes import router
from backend.core.config import settings
from database.database import engine
from backend.models.project import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.include_router(router)