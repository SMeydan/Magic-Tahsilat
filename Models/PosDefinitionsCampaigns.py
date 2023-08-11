from pydantic import BaseModel
from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, Date

from database import Base

class PosDefinitionsCampaignsBase(BaseModel):
    pos_definitions_id: str
    campaign_id: str

class PosDefinitionsCampaigns(Base):
    __tablename__ = "pos_definitions_campaigns"
    pos_definitions_id = Column(String,primary_key = True) 
    campaign_id = Column(String,primary_key = True)
    