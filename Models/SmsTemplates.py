from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class SmsTemplatesBase(BaseModel):
    id: str
    activity_status: bool
    template_name: str
    sending_activity_status: bool
    service_provider_id: str
    user_id: str
    password: str
    content: str

class SmsTemplates(Base):
    __tablename__ = "sms_templates"
    id = Column(String,primary_key = True) 
    activity_status = Column(Integer)
    template_name = Column(String)
    sending_activity_status = Column(Integer)
    service_provider_id = Column(String)
    user_id = Column(String)
    password = Column(String)
    content = Column(String)