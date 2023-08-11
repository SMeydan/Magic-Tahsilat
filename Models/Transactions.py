from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class TransactionsBase(BaseModel):
    id: str
    transaction_name: str

class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(String,primary_key = True) 
    transaction_name = Column(String)
    