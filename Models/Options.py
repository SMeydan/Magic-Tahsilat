from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class OptionsBase(BaseModel):
    id: str
    activity_status: bool
    default_value: str
    name: str

class Options(Base):
    __tablename__ = "options"
    id = Column(String,primary_key = True) 
    activity_status = Column(Integer)
    default_value = Column(String)
    name = Column(String)
    