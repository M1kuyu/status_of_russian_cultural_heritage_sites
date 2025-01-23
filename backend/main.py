import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, HTTPException, Depends, WebSocket
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select  # Import the select function
from sqlalchemy import text  # Import the text function
from app.database import SessionLocal, init_db
from app.models.heritage_site import HeritageSite
from app.models.user import User

from app.schemas.heritage_site import HeritageSiteSchema  # Import the schema
from passlib.context import CryptContext

app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.on_event("startup")
async def startup():
    await init_db()  # Await the init_db function

@app.get("/")
def root():
    return {"message": "Welcome to the Cultural Heritage Tracker"}

# Add a cultural site
@app.post("/sites/", response_model=HeritageSiteSchema)
async def add_site(site: HeritageSiteSchema, db: AsyncSession = Depends(get_db)):
    db_site = HeritageSite(**site.dict())
    db.add(db_site)
    await db.commit()
    await db.refresh(db_site)
    return db_site

# Get all cultural sites
@app.get("/sites/", response_model=List[HeritageSiteSchema])
async def get_sites(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(HeritageSite))  # Use select() for ORM
    sites = result.scalars().all()  # Get all results
    return [HeritageSiteSchema.from_orm(site) for site in sites]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post("/register/")
async def register_user(username: str, email: str, password: str, db: AsyncSession = Depends(get_db)):
    hashed_password = pwd_context.hash(password)
    user = User(username=username, email=email, hashed_password=hashed_password)  # Include email
    db.add(user)
    await db.commit()
    return {"message": "User registered successfully!"}

@app.websocket("/ws/notifications/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("Connected to notifications")
    await websocket.close()
