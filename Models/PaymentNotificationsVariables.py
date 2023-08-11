from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PaymentNotificationsVariablesBase(BaseModel):
    id: str
    payment_notifications_id: str
    variables_id: str

class PaymentNotificationsVariables(Base):
    __tablename__ = "payment_notifications_variables"
    id = Column(String,primary_key = True) 
    payment_notifications_id = Column(String) 
    variables_id = Column(String)