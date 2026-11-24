import pytest
from app import app, calculate_gross_price

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_calculate_gross_price():
    assert calculate_gross_price(1000)== 1270.0
    assert calculate_gross_price(0)== 0.0

def test_negative_price_raises_error():
    with pytest.raises(ValueError):
        calculate_gross_price(-100)

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status":"UP"}

def test_calculate_endpoint(client):
    response = client.get("/calculate?net=2000")
    assert response.status_code == 200
    assert response.get_json()["gross_price"]==2540.0