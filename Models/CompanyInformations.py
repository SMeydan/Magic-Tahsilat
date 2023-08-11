from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class CompanyInformationsBase(BaseModel):
    id: str
    company_name: str
    tax_office: str
    tax_number: str
    phone: str
    fax: str
    users_id: str
    mobile_phone: str
    email: str
    country_id: str
    city_id: str
    town_id: str
    district_id: str
    address: str

class CompanyInformations(Base):
    __tablename__ = "company_information"
    id = Column(String,primary_key = True)
    company_name = Column(String)
    tax_office = Column(String)
    tax_number = Column(String)
    phone = Column(String)
    fax = Column(String)
    users_id = Column(String)
    mobile_phone = Column(String)
    email = Column(String)
    country_id = Column(String)
    city_id = Column(String)
    town_id = Column(String)
    district_id = Column(String)
    address = Column(String)
