from fastapi import status
from fastapi.testclient import TestClient
from recept import app, get_db
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.pool import StaticPool
from adatmodell import uzletek_modell
import pytest
import json


SQLALCHEMY_DATABASE_URL = 'sqlite:///./test_recept.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}, poolclass=StaticPool,)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()

uzletek_modell.Base.metadata.create_all(bind=engine)


#@pytest.mark.filterwarnings("ignore:.*usage will be deprecated.*:DeprecationWarning")
# @pytest.mark.skip(reason="no way of currently testing this")
# def test_get_db():
def get_db_test():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()



app.dependency_overrides[get_db] = get_db_test
# app.dependency_overrides[get_db] = test_get_db

client = TestClient(app)


@pytest.fixture
def test_uzlet():
    uzlet = uzletek_modell.Uzletek(
        uzlet_id=1,
        uzlet_nev='Teszt üzlet'
    )
    db = TestingSessionLocal()
    db.add(uzlet)
    db.commit()
    yield uzlet
    
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM uzletek;"))
        connection.commit()
        

def test_read_all_uzletek():
    response = client.get("/test_case_uzletek")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []

    
def test_db_uzlet(test_uzlet):
    response = client.get("/test_case_uzletek")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'uzlet_id':1, 'uzlet_nev':'Teszt üzlet'}]



def test_case_uzlet_uj():
     
    uzlet={
        'uzlet_nev': 'Mocked üzlet'
    }

    response = client.post("/test_case_uzlet_uj", params=uzlet)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'uzlet_nev':'Mocked üzlet'}
    
    # MARK: DB-ből kérdezd le a sikeres rögzítést
    
    with engine.connect() as connection:
        connection.execute(text("DELETE FROM uzletek;"))
        connection.commit()