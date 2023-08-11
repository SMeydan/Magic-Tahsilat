from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PaymentOptionsBase(BaseModel):
    id: str
    payment_option_name: str
    service_description: str
    vat: float
    options_id: str
    amount_effect: str
    lower_limit: float
    upper_limit: float
    member_groups_id: str
    
class PaymentOptions(Base):
    __tablename__ = "payment_options"
    id = Column(String,primary_key = True) 
    payment_option_name = Column(String)
    service_description = Column(String)
    vat = Column(Float)
    options_id = Column(String)
    amount_effect = Column(String)
    lower_limit = Column(Float)
    upper_limit = Column(Float)
    member_groups_id = Column(String)