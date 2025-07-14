"""
Пример e2e-теста для API (pytest, requests)
"""
import pytest
import requests

def test_api_health():
    resp = requests.get("http://localhost:8000/health")
    assert resp.status_code == 200 