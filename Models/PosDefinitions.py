from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PosDefinitionsBase(BaseModel):
    id: str
    pos_information_id: str
    default: bool
    test_status: bool
    cvv_required: bool
    expiry: date
    single_payment_commission: float
    threeD: str
    threeD_model: str
    threeD_limit: str
    currency_id: str
    merchant_number: str
    username: str
    threeD_key: str
    notification_url: str
    ipn_address: str
    store_code_normal_transaction: str
    encoding_key_normal_transaction: str
    store_code_3d_transaction: str
    encoding_key_3d_transaction: str
    api_key: str
    secret_key: str
    merchant_id: str
    merchant_key: str
    app_id: str
    app_secret: str
    webhook_key: str
    webhook_url: str

class PosDefinitions(Base):
    __tablename__ = "pos_definitions"
    id = Column(String,primary_key = True) 
    pos_information_id = Column(String)
    default = Column(Integer)
    test_status = Column(Integer)
    cvv_required = Column(Integer)
    expiry = Column(Date)
    single_payment_commission = Column(Float)
    threeD = Column(String)
    threeD_model = Column(String)
    threeD_limit = Column(String)
    currency_id = Column(String)
    merchant_number = Column(String)
    username = Column(String)
    threeD_key = Column(String)
    notification_url = Column(String)
    ipn_address = Column(String)
    store_code_normal_transaction = Column(String)
    encoding_key_normal_transaction = Column(String)
    store_code_3d_transaction = Column(String)
    encoding_key_3d_transaction = Column(String)
    api_key = Column(String)
    secret_key = Column(String)
    merchant_id = Column(String)
    merchant_key = Column(String)
    app_id = Column(String)
    app_secret = Column(String)
    webhook_key = Column(String)
    webhook_url = Column(String)