import requests

def test_api_responde():
    url = "https://api-evidencia2.duckdns.org"
    response = requests.get(url)
    assert response.status_code == 200
    assert "API Fase 1 funcionando!" in response.text
