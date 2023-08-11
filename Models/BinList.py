from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from datetime import date

from database import Base


class BinListBase(BaseModel):
    id: str
    bin: str
    bank_id: str
    brand: str
    card_type: str
    hit: str
    last_request_date: date
    commercial_card_status: str

class BinList(Base):
    __tablename__ = "binlist"
    id = Column(String,primary_key = True)
    bin = Column(String)
    bank_id = Column(String)
    brand = Column(String)
    card_type = Column(String)
    hit = Column(String)
    last_request_date = Column(Date)
    commercial_card_status = Column(String)