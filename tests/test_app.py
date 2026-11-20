"""
Тесты прототипа TaskTracker (ЛР 7).
Проверяют создание и завершение задачи через тестовый клиент Flask.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_task(client):
    """Создание новой задачи возвращает 201 и задачу с полями."""
    resp = client.post("/tasks", json={"title": "Купить хлеб"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "Купить хлеб"
    assert data["done"] is False
    assert "id" in data


def test_complete_task(client):
    """Пометка задачи выполненной меняет done на True."""
    client.post("/tasks", json={"title": "Позвонить маме"})
    resp = client.post("/tasks/1/complete")
    assert resp.status_code == 200
    assert resp.get_json()["done"] is True
