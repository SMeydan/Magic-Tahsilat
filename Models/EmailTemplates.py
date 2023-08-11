from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class EmailTemplatesBase(BaseModel):
    id: str
    activity_status: bool
    template_name: str
    sender_email: str
    recipient_email: str
    cc_email: str
    bcc_email: str
    topic: str
    content: str

class EmailTemplates(Base):
    __tablename__ = "email_templates"
    id = Column(String,primary_key = True) 
    activity_status = Column(Integer)
    template_name = Column(String)
    sender_email = Column(String)
    recipient_email = Column(String)
    cc_email = Column(String)
    bcc_email = Column(String)
    topic = Column(String)
    content = Column(String)