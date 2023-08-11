from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PaymentNotificationsBase(BaseModel):
    id: str
    members_id: str
    amount: float
    payment_set_id: str
    validity_period: date
    threeD_security_type: str
    activation_status: bool
    single_use: bool
    unregistered: bool
    fixed_price: bool
    fixed_description: bool
    show_description: bool
    explanation: str
    email_subject: str
    templates: str
    email_content: str
    send_sms: bool

class PaymentNotifications(Base):
    __tablename__ = "payment_notifications"
    id = Column(String,primary_key = True) 
    members_id = Column(String)
    amount = Column(Float)
    payment_set_id = Column(String)
    validity_period = Column(Date)
    threeD_security_type = Column(String)
    activation_status = Column(Integer)
    single_use = Column(Integer)
    unregistered = Column(Integer)
    fixed_price = Column(Integer)
    fixed_description = Column(Integer)
    show_description = Column(Integer)
    explanation = Column(String)
    email_subject = Column(String)
    templates = Column(String)
    email_content = Column(String)
    send_sms = Column(Integer)
    