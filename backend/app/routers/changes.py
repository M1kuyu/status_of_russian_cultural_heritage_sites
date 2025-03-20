from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.models.change_log import ChangeLog
from app.schemas.change_log import ChangeLogSchema
from app.database import get_db

router = APIRouter()

@router.get("/changes/", response_model=List[ChangeLogSchema])
async def get_changes(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(ChangeLog))
    changes = result.scalars().all()
    return changes
