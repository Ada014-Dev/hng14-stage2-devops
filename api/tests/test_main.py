from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with patch("redis.Redis.from_url") as mock_redis:
    mock_redis.return_value = MagicMock()
    from main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_job():
    with patch("main.r") as mock_r:
        mock_r.lpush = MagicMock()
        mock_r.hset = MagicMock()
        response = client.post("/jobs")
        assert response.status_code == 200
        assert "job_id" in response.json()


def test_get_job_not_found():
    with patch("main.r") as mock_r:
        mock_r.hget = MagicMock(return_value=None)
        response = client.get("/jobs/fake-id")
        assert response.status_code == 200
        assert response.json() == {"error": "not found"}
