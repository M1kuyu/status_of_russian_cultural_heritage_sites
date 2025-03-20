from sqlalchemy import Column, BigInteger, VARCHAR, Enum, Date, Integer, Index
from app.database import Base

class ChangeLog(Base):
    __tablename__ = "change_log"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    global_id = Column(BigInteger, nullable=False)
    field_name = Column(VARCHAR(255), nullable=False)
    old_value = Column(VARCHAR(4000), default=None)
    new_value = Column(VARCHAR(4000), default=None)
    status = Column(Enum('Добавлено', 'Удалено', 'Изменено'), nullable=False)
    change_date = Column(Date, nullable=False)
    dataset_version = Column(Integer, nullable=False)
    ObjectNameOnDoc = Column(VARCHAR(4000), default=None)
    Addresses = Column(VARCHAR(4000), default=None)

    __table_args__ = (
        Index('idx_global_id', 'global_id'),
        Index('idx_change_date', 'change_date'),
    )
