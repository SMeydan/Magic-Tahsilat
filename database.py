from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from decouple import config

DATABASE_HOST = config("DATABASE_HOST")
DATABASE_USER = config("DATABASE_USER")
DATABASE_NAME = config("DATABASE_NAME")
DATABASE_PWD = config("DATABASE_PWD")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PWD}@{DATABASE_HOST}/{DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
