from sqlalchemy import Column, ForeignKey, Integer

from src.db.models.base import Base

class Industry(Base):
    __tablename__ = "industries"

    industry_id = Column(Integer, primary_key=True, autoincrement=True)
    sector_id = Column(Integer, ForeignKey("sectors.sector_id"))


########################################################
#
def get_or_create_industry(session, name, sector_id):
    industry = session.query(Industry).filter_by(name=name).first()
    if industry is None:
        industry = Industry(name=name, sector_id=sector_id)
        session.add(industry)
        session.commit()
    return industry