from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection settings
DATABASE_USERNAME = "root"  # Default username for XAMPP
DATABASE_PASSWORD = ""      # Default password for XAMPP
DATABASE_HOST = "localhost" # Localhost for XAMPP
DATABASE_PORT = "3306"      # Default port for MySQL in XAMPP
DATABASE_NAME = "cultural_sites"

# Database URL in SQLAlchemy format
DATABASE_URL = f"mysql+aiomysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Create the SQLAlchemy asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory for AsyncSession
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# Base class for defining ORM models
Base = declarative_base()

# Initialize the database
async def init_db():
    """
    Initializes the database by creating all tables defined in the models.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session
