from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TransactionsBase(BaseModel):
    id: str
    transaction_name: str

class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(String,primary_key = True) 
    transaction_name = Column(String)
    