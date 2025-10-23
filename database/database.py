from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declared_attr
from sqlalchemy.ext.declarative import declarative_base

# class BaseWithSchema:
#     @declared_attr
#     def __table_args__(cls):
#         return {'schema': 'local'}

DATABASE = "postgresql://postgres:2716@localhost:5432/postgres"
SCHEMA = "public"
DATABASE_URL = f"{DATABASE}?options=-c%20search_path={SCHEMA}"
engine = create_engine(DATABASE_URL)
# Base = declarative_base(cls=BaseWithSchema)
Base = declarative_base()
SessionLocal = sessionmaker(autoflush=False, bind=engine,autocommit=False)