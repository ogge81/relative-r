from sqlalchemy import Column, Integer

from src.db.models.base import Base


class Sector(Base):
    __tablename__ = "sectors"

    sector_id = Column(Integer, primary_key=True, autoincrement=True)


########################################################
#
def get_or_create_sector(session, name):
    sector = session.query(Sector).filter_by(name=name).first()
    if sector is None:
        sector = Sector(name=name)
        session.add(sector)
        session.commit()
    return sector