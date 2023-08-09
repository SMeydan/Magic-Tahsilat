from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class InstallmentsBase(BaseModel):
    id: str
    banks_id: str
    brand: str
    installment: str
    member_group_id: str
    commission: str
    commercial_card_commission: float
    upper_limit: float
    status: str
    commercial_card_status: str
    pos_id: str
    additional_installment: int
    additional_installment_limit: float
    additional_installment_upper_limit: float
    payment_set_id: str
    expiry: date

class Installments(Base):
    __tablename__ = "installments"
    id = Column(String,primary_key = True) 
    banks_id = Column(String)
    brand = Column(String)
    installment = Column(String)
    member_group_id = Column(String)
    commission = Column(String)
    commercial_card_commission = Column(Float)
    upper_limit = Column(Float)
    status = Column(String)
    commercial_card_status = Column(String)
    pos_id = Column(String)
    additional_installment = Column(Integer)
    additional_installment_limit = Column(Float)
    additional_installment_upper_limit = Column(Float)
    payment_set_id = Column(String)
    expiry = Column(Date)    