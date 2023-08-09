from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PaymentPageFormBase(BaseModel):
    id: str
    field_name: str
    name: str
    type: str
    record_visibility_status: bool
    record_requirement_status: bool
    update_visibility_status: bool
    update_requirement_status: bool
    max_character: int
    min_character: int
    unwanted_character: str
    options: str

class PaymentPageForm(Base):
    __tablename__ = "payment_page_form"
    id = Column(String,primary_key = True) 
    field_name = Column(String)
    name = Column(String)
    type = Column(String)
    record_visibility_status = Column(Integer)
    record_requirement_status = Column(Integer)
    update_visibility_status = Column(Integer)
    update_requirement_status = Column(Integer)
    max_character = Column(Integer)
    min_character = Column(Integer)
    unwanted_character = Column(String)
    options = Column(String)