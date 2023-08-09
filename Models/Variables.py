from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VariablesBase(BaseModel):
    id: str
    variable: str
    variable_query: str

class Variables(Base):
    __tablename__ = "variables"
    id = Column(String,primary_key = True) 
    variable = Column(String)
    variable_query = Column(String)    