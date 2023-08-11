from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PosInformationBase(BaseModel):
    id: str
    pos_name: str
    pos_type: str
    company_information_id: str
    model: str

class PosInformation(Base):
    __tablename__ = "pos_information"
    id = Column(String,primary_key = True) 
    pos_name = Column(String)
    pos_type = Column(String)
    company_information_id = Column(String)
    model = Column(String)