from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from database import Base


class CitiesBase(BaseModel):
    id: str
    country_id: str
    cities: str
    
class Cities(Base):
    __tablename__ = "cities"
    id = Column(String,primary_key = True)
    country_id = Column(String)
    cities = Column(String)