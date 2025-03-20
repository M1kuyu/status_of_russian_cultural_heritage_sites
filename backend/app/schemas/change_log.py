from pydantic import BaseModel
from datetime import date
from typing import Optional

class ChangeLogSchema(BaseModel):
    id: int
    global_id: int
    field_name: str
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    status: str
    change_date: date
    dataset_version: int
    ObjectNameOnDoc: Optional[str] = None
    Addresses: Optional[str] = None

    class Config:
        orm_mode = True
