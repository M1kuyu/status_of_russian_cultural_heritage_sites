from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from models import Changes  # Import your Changes model
from schemas import ChangesSchema  # Create a ChangesSchema in your schemas.py
from database import get_db

router = APIRouter()

@router.get("/changes/", response_model=List[ChangesSchema])
async def get_changes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Changes))
    changes = result.scalars().all()
    return [ChangesSchema.from_orm(change) for change in changes]
