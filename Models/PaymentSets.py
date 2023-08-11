from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PaymentSetsBase(BaseModel):
    id: str
    payment_set_name: str
    activity_status: bool
    member_group_status: bool
    warning_text: str

class PaymentSets(Base):
    __tablename__ = "payment_sets"
    id = Column(String,primary_key = True) 
    payment_set_name = Column(String)
    activity_status = Column(Integer)
    member_group_status = Column(Integer)
    warning_text = Column(String)    