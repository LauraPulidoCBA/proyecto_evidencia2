import pytest
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"API Fase 1 funcionando! - actualizado" in response.data

