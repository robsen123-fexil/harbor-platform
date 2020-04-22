from harbor.api.app import create_app
from fastapi.testclient import TestClient


def test_health() -> None:
    client = TestClient(create_app())
    assert client.get("/health").json()["status"] == "up"
