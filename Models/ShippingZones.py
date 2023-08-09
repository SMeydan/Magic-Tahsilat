from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ShippingZonesBase(BaseModel):
    id: str
    shipping_zone_name: str

class ShippingZones(Base):
    __tablename__ = "shipping_zones"
    id = Column(String,primary_key = True) 
    shipping_zone_name = Column(String)
    