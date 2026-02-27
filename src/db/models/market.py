from sqlalchemy import Column, Integer, String

from src.db.models.base import Base

class Market(Base):
    __tablename__ = "markets"
    
    market_id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String)

def create_market():
    pass

def get_market(market_id: int):
    pass