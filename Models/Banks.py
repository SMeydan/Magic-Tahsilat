from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from database import Base

class BanksBase(BaseModel):
    id: str
    bank_name: str
    default_single_installment_pos_id: str
    default_installment_pos_id: str
    single_installment_due_date: int
    single_installment_commission: float
    logo: str
    color: str

class Banks(Base):
    __tablename__ = "banks"
    id = Column(String,primary_key = True)
    bank_name = Column(String)
    default_single_installment_pos_id = Column(String)
    default_installment_pos_id = Column(String)
    single_installment_due_date = Column(Integer) 
    single_installment_commission = Column(Float)
    logo = Column(String)
    color = Column(String)
    

