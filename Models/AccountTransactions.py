from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from datetime import date

from database import Base


class AccountTransactionsBase(BaseModel):
    id: str
    members_id: str
    date: date
    submember_id: str
    transaction_number: str
    document_number: str
    explanation: str
    debt: float
    receivable: float
    balance: float
    usd_debt: float
    usd_receivable: float
    usd_balance: float


class AccountTransactions(Base):
    __tablename__ = "account_transactions"

    id = Column(String, primary_key=True)
    members_id = Column(String)
    date = Column(Date)
    submember_id = Column(String)
    transaction_number = Column(String)
    document_number = Column(String)
    explanation = Column(String)
    debt = Column(Float)
    receivable = Column(Float)
    balance = Column(Float)
    usd_debt = Column(Float)
    usd_receivable = Column(Float)
    usd_balance = Column(Float)
