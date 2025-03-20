import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException, Depends, WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text
from app.database import SessionLocal, init_db
from app.models.heritage_site import HeritageSite
from app.schemas.heritage_site import HeritageSiteSchema
from passlib.context import CryptContext

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL вашего фронтенда
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключение роутера для журнала изменений
from app.routers import changes
app.include_router(changes.router)

# Dependency для получения сессии БД
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
def root():
    return {"message": "Welcome to the Cultural Heritage Tracker"}

# Добавление объекта культурного наследия
@app.post("/sites/", response_model=HeritageSiteSchema)
async def add_site(site: HeritageSiteSchema, db: AsyncSession = Depends(get_db)):
    db_site = HeritageSite(**site.dict())
    db.add(db_site)
    await db.commit()
    await db.refresh(db_site)
    return db_site

# Получение всех объектов культурного наследия
@app.get("/sites/", response_model=List[HeritageSiteSchema])
async def get_sites(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(HeritageSite))
    sites = result.scalars().all()
    return [HeritageSiteSchema.from_orm(site) for site in sites]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
