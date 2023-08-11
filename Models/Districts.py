from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class DistrictsBase(BaseModel):
    id: str
    town_id: str
    districts: str

class Districts(Base):
    __tablename__ = "districts"
    id = Column(String,primary_key = True) 
    town_id = Column(String)
    districts = Column(String)