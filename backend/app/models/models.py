from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, JSON, BigInteger, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()

# Users Table
class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# Heritage Sites Table
class HeritageSite(Base):
    __tablename__ = 'heritage_sites_1'

    id = Column(Integer, primary_key=True, autoincrement=True)
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
    global_id = Column(BigInteger)  # Уникальный идентификатор
    geoData = Column(JSON)  # Геоданные в формате JSON
    geodata_center = Column(JSON)  # Центр геоданных в формате JSON

    def __repr__(self):
        return f"<HeritageSite(id={self.id}, ObjectNameOnDoc='{self.ObjectNameOnDoc}')>"

