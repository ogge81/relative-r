from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer

from src.db.models.base import Base


class PriceRow(Base):
    __tablename__ = "pricerows"

    pricerow_id = Column(Integer, primary_key=True, autoincrement=True)
    asset_id = Column(Integer, ForeignKey("assets.asset_id"))

    datetime = Column(DateTime)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)