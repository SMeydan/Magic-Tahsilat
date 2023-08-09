from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShippingCompaniesBase(BaseModel):
    id: str
    shipping_company_name: str
    calculation_type: str
    integrated: bool
    member_groups_id: str
    free_limit: float
    member_group_status: str
    payment_method: str
    activity_status: bool
    default_value: str
    regional: str
    tariff_id: str
    country_city_id: str

class ShippingCompanies(Base):
    __tablename__ = "shipping_companies"
    id = Column(String,primary_key = True) 
    shipping_company_name = Column(String)
    calculation_type = Column(String)
    integrated = Column(Integer)
    member_groups_id = Column(String)
    free_limit = Column(Float)
    member_group_status = Column(String)
    payment_method = Column(String)
    activity_status = Column(Integer)
    default_value = Column(String)
    regional = Column(String)
    tariff_id = Column(String)
    country_city_id = Column(String)