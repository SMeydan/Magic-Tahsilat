from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TariffsBase(BaseModel):
    id: str
    tariff_name: str
    lower_limit: float
    out_of_country_status: bool
    out_of_city_status: bool
    in_city_status: bool

class Tariffs(Base):
    __tablename__ = "tariffs"
    id = Column(String,primary_key = True) 
    tariff_name = Column(String)
    lower_limit = Column(Float)
    out_of_country_status = Column(Integer)
    out_of_city_status = Column(Integer)
    in_city_status = Column(Integer)