from adatbazis.adatbazis import Base
from sqlalchemy import Column, Integer, String, Boolean

class Uzletek(Base):
    __tablename__ = 'uzletek'
    
    uzlet_id  = Column(Integer, primary_key=True, index=True)
    uzlet_nev = Column(String)