from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class SmsTemplatesVariablesBase(BaseModel):
    variables_id: str
    sms_templates_id: str

class SmsTemplatesVariables(Base):
    __tablename__ = "sms_templates_variables"
    variables_id = Column(String,primary_key = True) 
    sms_templates_id = Column(String,primary_key = True)