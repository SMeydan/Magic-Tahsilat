from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

Base = declarative_base()

class CollectionTemplatesBase(BaseModel):
    id: str
    template_name: str
    amount: float
    payment_frequency: str
    payment_period: str
    payment_count: int
    explanation: str
    make_first_payment: bool
    fixed_description: bool

class CollectionTemplates(Base):
    __tablename__ = "collection_templates"
    id = Column(String,primary_key = True)
    template_name = Column(String)
    amount = Column(Float)
    payment_frequency = Column(String)
    payment_period = Column(String)
    payment_count = Column(Integer)
    explanation = Column(String)
    make_first_payment = Column(Boolean)
    fixed_description = Column(Boolean)
