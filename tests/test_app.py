from fastapi.testclient import TestClient

from src.app.main import app, model

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_loads():
    assert model is not None


def test_valid_prediction():
    response = client.post(
        "/predict",
        json={
            "tenure_months": 12,
            "monthly_fee": 45.5,
            "support_calls": 2,
            "contract": "Month-to-month",
            "internet_service": "Fiber optic"
        }
    )

    assert response.status_code == 200
    assert "prediction" in response.json()


def test_invalid_input_schema():
    response = client.post(
        "/predict",
        json={
            "tenure_months": "wrong",
            "monthly_fee": 45.5,
            "support_calls": 2,
            "contract": "Month-to-month",
            "internet_service": "Fiber optic"
        }
    )

    assert response.status_code == 422


def test_deterministic_prediction():
    data = {
        "tenure_months": 12,
        "monthly_fee": 45.5,
        "support_calls": 2,
        "contract": "Month-to-month",
        "internet_service": "Fiber optic"
    }

    response1 = client.post("/predict", json=data)
    response2 = client.post("/predict", json=data)

    assert response1.json() == response2.json()