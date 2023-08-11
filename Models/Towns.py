from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class TownsBase(BaseModel):
    id: str
    city_id: str
    towns: str  

class Towns(Base):
    __tablename__ = "towns"
    id = Column(String,primary_key = True) 
    city_id = Column(String)
    towns = Column(String)