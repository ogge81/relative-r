from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import session
from sqlalchemy.util import symbol

from src.db.models.base import Base

class Asset(Base):
    __tablename__ = "assets"

    asset_id = Column(Integer, primary_key=True, autoincrement=True)
    sector_id = Column(Integer, ForeignKey("sectors.sector_id"))
    industry_id = Column(Integer, ForeignKey("industries.industry_id"))

    name = Column(String)
    symbol = Column(String, unique=True)
    market_cap = Column(Float)
    previous_close = Column(Float)
    last_volume = Column(Integer)

def get_or_create_asset(session, symbol):
    asset = session.query(Asset).filter_by(symbol=symbol).first()
    if asset is None:
        asset = Asset(symbol=symbol)
        session.add(asset)
        session.commit()
    return asset