from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ServiceProvidersBase(BaseModel):
    id: str
    service_provider_name: str

class ServiceProviders(Base):
    __tablename__ = "service_providers"
    id = Column(String,primary_key = True) 
    service_provider_name = Column(String)