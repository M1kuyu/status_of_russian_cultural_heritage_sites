from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, JSON, BigInteger, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()


# Heritage Sites Table
class HeritageSite(Base):
    __tablename__ = 'data_530_2025_03_05_289_xlsx___0'

    ObjectNameOnDoc = Column(Text)  # Наименование объекта по документам
    AISID = Column(String(36))  # Идентификатор в АИС Мосгорнаследия (UUID stored as string)
    USRCHONumber = Column(String(50))  # Номер ЕГРОКН
    ObjectName = Column(Text)  # Общепринятое наименование объекта
    EnsembleNameOnDoc = Column(Text)  # Наименование ансамбля по документам
    EnsembleName = Column(Text)  # Общепринятое наименование ансамбля
    AdmArea = Column(Text)  # Административный округ
    District = Column(Text)  # Район
    Location = Column(Text)  # Местоположение объекта
    Addresses = Column(Text)  # Полный список адресов
    SecurityStatus = Column(Text)  # Охранный статус
    Category = Column(Text)  # Категория объекта
    ObjectType = Column(Text)  # Вид объекта недвижимости
    global_id = Column(BigInteger, primary_key=True)  # Уникальный идентификатор

    def __repr__(self):
        return f"<HeritageSite(id={self.id}, ObjectNameOnDoc='{self.ObjectNameOnDoc}')>"

