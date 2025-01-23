from pydantic import BaseModel
from typing import Optional

class HeritageSiteSchema(BaseModel):
    id: int
    ObjectNameOnDoc: Optional[str]
    AISID: Optional[str]
    USRCHONumber: Optional[str]
    ObjectName: Optional[str]
    EnsembleNameOnDoc: Optional[str]
    EnsembleName: Optional[str]
    AdmArea: Optional[str]
    District: Optional[str]
    Location: Optional[str]
    Addresses: Optional[str]
    SecurityStatus: Optional[str]
    Category: Optional[str]
    ObjectType: Optional[str]
    global_id: Optional[int]
    geoData: Optional[dict]
    geodata_center: Optional[dict]

    class Config:
        from_attributes = True  # Replaces orm_mode in Pydantic v2
