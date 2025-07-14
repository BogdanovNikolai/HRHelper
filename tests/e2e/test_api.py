"""
E2E-тесты для FastAPI API (pytest, httpx)
"""
import pytest
import httpx

BASE_URL = "http://localhost:8000"

def test_health():
    resp = httpx.get(f"{BASE_URL}/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_hh_resumes():
    resp = httpx.get(f"{BASE_URL}/hh/resumes")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert data and "id" in data[0] and "name" in data[0]

def test_avito_vacancies():
    resp = httpx.get(f"{BASE_URL}/avito/vacancies")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert data and "id" in data[0] and "title" in data[0] 