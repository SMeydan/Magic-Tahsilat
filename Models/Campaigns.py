from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from database import Base


class CampaignsBase(BaseModel):
    id: str
    campaign_name: str
    installment: str
    payment_set_id: str
    commission: str
    commercial_card_commission: str
    sequence_number: str

class Campaigns(Base):
    __tablename__ = "campaigns"
    id = Column(String,primary_key = True)
    campaign_name = Column(String)
    installment = Column(String)
    payment_set_id = Column(String)
    commission = Column(String)
    commercial_card_commission = Column(String)
    sequence_number = Column(String)