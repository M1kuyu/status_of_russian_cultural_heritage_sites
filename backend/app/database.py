from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection settings
DATABASE_USERNAME = "root"  # Default username for XAMPP
DATABASE_PASSWORD = ""      # Default password for XAMPP
DATABASE_HOST = "localhost" # Localhost for XAMPP
DATABASE_PORT = "3306"      # Default port for MySQL in XAMPP
DATABASE_NAME = "cultural_sites"

# Database URL in SQLAlchemy format
DATABASE_URL = f"mysql+pymysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for defining ORM models
Base = declarative_base()

# Initialize the database
def init_db():
    """
    Initializes the database by creating all tables defined in the models.
    """
    from .models import HeritageSite, User  # Import your models here
    Base.metadata.create_all(bind=engine)
