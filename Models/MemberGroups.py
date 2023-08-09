from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MemberGroupsBase(BaseModel):
    id: str
    member_group_name: str

class MemberGroups(Base):
    __tablename__ = "member_groups"
    id = Column(String,primary_key = True) 
    member_group_name = Column(String)  