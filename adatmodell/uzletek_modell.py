from adatbazis.adatbazis import Base
from sqlalchemy import Column, Integer, String, Boolean, BIGINT, VARCHAR, INT
from sqlalchemy.orm import Mapped, mapped_column

# class Uzletek(Base):
#     __tablename__ = 'uzletek'
    
#     uzlet_id  = Column(Integer, primary_key=True, index=True)
#     uzlet_nev = Column(String)
    
    
class Uzletek(Base):
    __tablename__ = 'uzletek'
    
    uzlet_id: Mapped[int]  = mapped_column(INT, primary_key=True, index=True, autoincrement=True)
    uzlet_nev: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)