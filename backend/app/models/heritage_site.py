from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class HeritageSite(Base):
    __tablename__ = "data_530_2025_03_05_289_xlsx___0"

    ObjectNameOnDoc = Column(String, nullable=True)
    AISID = Column(String, nullable=True)
    USRCHONumber = Column(String, nullable=True)
    ObjectName = Column(String, nullable=True)
    EnsembleNameOnDoc = Column(String, nullable=True)
    EnsembleName = Column(String, nullable=True)
    AdmArea = Column(String, nullable=True)
    District = Column(String, nullable=True)
    Location = Column(String, nullable=True)
    Addresses = Column(String, nullable=True)
    SecurityStatus = Column(String, nullable=True)
    Category = Column(String, nullable=True)
    ObjectType = Column(String, nullable=True)
    global_id = Column(Integer, primary_key=True, index=True)

