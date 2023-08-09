from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class EmailTemplatesVariablesBase(BaseModel):
    email_templates_id: str
    variables_id: str

class EmailTemplatesVariables(Base):
    __tablename__ = "email_templates_variables"
    email_templates_id = Column(String,primary_key = True) 
    variables_id = Column(String,primary_key = True)
    