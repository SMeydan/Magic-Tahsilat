from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserAuthorizationsBase(BaseModel):
    id: str
    transaction_group: str
    transactions_id: str
    status: str

class UserAuthorizations(Base):
    __tablename__ = "user_authorizations"
    id = Column(String,primary_key = True) 
    transaction_group = Column(String)
    transactions_id = Column(String)
    status = Column(String)