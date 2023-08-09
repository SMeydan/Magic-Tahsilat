from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SmsTemplatesVariablesBase(BaseModel):
    variables_id: str
    sms_templates_id: str

class SmsTemplatesVariables(Base):
    __tablename__ = "sms_templates_variables"
    variables_id = Column(String,primary_key = True) 
    sms_templates_id = Column(String,primary_key = True)