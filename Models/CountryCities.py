from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date,Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class CountryCitiesBase(BaseModel):
    id: str
    country_code: str
    country: str
    shipping_zone_id: str
    state_status: bool
    status: str

class CountryCities(Base):
    __tablename__ = "country_cities"
    id = Column(String,primary_key = True)
    country_code = Column(String)
    country = Column(String)
    shipping_zone_id = Column(String)
    state_status = Column(Boolean)
    status = Column(String)