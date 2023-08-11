from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class LanguageManagementBase(BaseModel):
    id: str
    language_code: str
    alignment: str
    language_name: str
    shortest_code: str
    icon_path: str
    decimal_symbol: str
    decimal_places: int
    thousands_separator: str
    first_day_of_week: str
    date: str
    long_date: str
    short_date: str
    long_time: str

class LanguageManagement(Base):
    __tablename__ = "language_management"
    id = Column(String,primary_key = True) 
    language_code = Column(String)
    alignment = Column(String)
    language_name = Column(String)
    shortest_code = Column(String)
    icon_path = Column(String)
    decimal_symbol = Column(String)
    decimal_places = Column(Integer)
    thousands_separator = Column(String)
    first_day_of_week = Column(String)
    date = Column(String)
    long_date = Column(String)
    short_date = Column(String)
    long_time = Column(String)