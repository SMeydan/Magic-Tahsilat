from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PeriodicCollectionBase(BaseModel):
    id: str
    members_id: str
    name: str
    credit_card_id: str
    registration_date: date
    start_date: date
    collection_templates_id: str

class PeriodicCollection(Base):
    __tablename__ = "periodic_collection"
    id = Column(String,primary_key = True) 
    members_id = Column(String) 
    name = Column(String)
    credit_card_id = Column(String)
    registration_date = Column(Date)
    start_date = Column(Date)
    collection_templates_id = Column(String)   