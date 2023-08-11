from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class CountriesBase(BaseModel):
    id: str
    country: str

class Countries(Base):
    __tablename__ = "countries"
    id = Column(String,primary_key = True)
    country = Column(String)