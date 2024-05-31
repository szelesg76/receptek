from fastapi.testclient import TestClient
import recept
from fastapi import status

client = TestClient(recept.app)


def test_return_health_check():
    response = client.get("/healthy")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'Healthy'}