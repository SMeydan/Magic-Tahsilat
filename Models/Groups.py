from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

from database import Base

class GroupsBase(BaseModel):
    id: str
    group_name: str
    ip: str
    is_api_user: bool
    user_authorizations_id: str
    
class Groups(Base):
    __tablename__ = "groups"
    id = Column(String,primary_key = True) 
    group_name = Column(String)
    ip = Column(String)
    is_api_user = Column(Integer)
    user_authorizations_id = Column(String)