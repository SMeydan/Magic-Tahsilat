from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class CreditCardsBase(BaseModel):
    id: str
    bank_id: str
    brand: str

class CreditCards(Base):
    __tablename__ = "countries"
    id = Column(String,primary_key = True)
    bank_id = Column(String)
    brand = Column(String)