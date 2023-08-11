from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class MembersBase(BaseModel):
    id: str
    member_description: str
    name: str
    surname: str
    identity_number: str
    company_name: str
    tax_office: str
    tax_number: str
    mobile_phone: str
    phone: str
    fax: str
    postal_code: str
    country_id: str
    city_id: str
    town_id: str
    district_id: str
    address: str
    ws_code: str
    customer_code: str
    submember_opening_permission: bool
    submember_creation_permission: bool
    submember_payment_notification_permission: bool
    can_create_payment_notification: bool
    submember_credit_authorization: bool
    can_enter_creditability: bool
    member_group_id: str
    representative_id: str
    max_receivable_limit: float
    max_debt_limit: float
    email: str
    password: str
    balance: float
    banned_status: bool
    risk_status: bool
    approval_status: bool

class Members(Base):
    __tablename__ = "members"
    id = Column(String,primary_key = True) 
    member_description = Column(String)
    name = Column(String)
    surname = Column(String)
    identity_number = Column(String)
    company_name = Column(String)
    tax_office = Column(String)
    tax_number = Column(String)
    mobile_phone = Column(String)
    phone = Column(String)
    fax = Column(String)
    postal_code = Column(String)
    country_id = Column(String)
    city_id = Column(String)
    town_id = Column(String)
    district_id = Column(String)
    address = Column(String)
    ws_code = Column(String)
    customer_code = Column(String)
    submember_opening_permission = Column(Integer)
    submember_creation_permission = Column(Integer)
    submember_payment_notification_permission = Column(Integer)
    can_create_payment_notification = Column(Integer)
    submember_credit_authorization = Column(Integer)
    can_enter_creditability = Column(Integer)
    member_group_id = Column(String)
    representative_id = Column(String)
    max_receivable_limit = Column(Float)
    max_debt_limit = Column(Float)
    email = Column(String)
    password = Column(String)
    balance = Column(Float)
    banned_status = Column(Integer)
    risk_status = Column(Integer)
    approval_status = Column(Integer)
