from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# from sqlalchemy.ext.declarative import declarative_base
# To
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_recept.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()