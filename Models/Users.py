from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UsersBase(BaseModel):
    id: str
    name: str
    surname: str
    identity_number: str
    username: str
    password: str
    webservice_code: str
    group_id: str
    role: str
    email: str
    phone: str
    iban: str
    photo: str
    country_id: str
    city_id: str
    town_id: str
    district_id: str
    address: str
    is_active: bool



class Users(Base):
    __tablename__ = "users"
    id = Column(String,primary_key = True) 
    name = Column(String)
    surname = Column(String)
    identity_number = Column(String)
    username = Column(String)
    password = Column(String)
    webservice_code = Column(String)
    group_id = Column(String)
    role = Column(String)
    email = Column(String)
    phone = Column(String)
    iban = Column(String)
    photo = Column(String)
    country_id = Column(String)
    city_id = Column(String)
    town_id = Column(String)
    district_id = Column(String)
    address = Column(String)
    is_active = Column(Boolean)