from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class CreditCardsBase(BaseModel):
    id: str
    bank_id: str
    brand: str

class CreditCards(Base):
    __tablename__ = "credit_cards"
    id = Column(String,primary_key = True)
    bank_id = Column(String)
    brand = Column(String)