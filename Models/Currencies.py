from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class CurrenciesBase(BaseModel):
    id: str
    currency_code: str
    currency_name: str
    default_currency: str
    status: str
    currency_rate: str

class Currencies(Base):
    __tablename__ = "currencies"
    id = Column(String,primary_key = True)
    currency_code = Column(String)
    currency_name = Column(String)
    default_currency = Column(String)
    status = Column(String)
    currency_rate = Column(String)

