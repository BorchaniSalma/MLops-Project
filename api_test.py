"""
API test file
"""

import pytest
from fastapi.testclient import TestClient
from main import api
import warnings
warnings.filterwarnings("ignore")


@pytest.fixture
def client():
    api_client = TestClient(api)
    return api_client


def test_get(client):
    r = client.get('/')

    assert r.status_code == 200
    assert r.json()['message'] == "Welcome !!"


def test_post_over_50(client):
    r = client.post("/infer", json={
        "age": 56,
        'fnlgt': 216851,
        'educationNum': 13,
        'capitalGain': 0,
        'capitalLoss': 0,
        "workclass": "Local-gov",
        "education": "Bachelors",
        "maritalStatus": "Married-civ-spouse",
        "occupation": "Tech-support",
        "relationship": "Husband",
        "race": "White",
        "sex": "Male",
        "hoursPerWeek": 40,
        "nativeCountry": "United-States"
    })
    assert r.status_code == 200
    assert r.json()['prediction'] == ">50K"


def test_post_under_50(client):
    r = client.post("/infer", json={
        "age": 34,
        'fnlgt': 245487,
        'educationNum': 4,
        'capitalGain': 0,
        'capitalLoss': 0,
        "workclass": "Private",
        "education": "7th-8th",
        "maritalStatus": "Married-civ-spouse",
        "occupation": "Transport-moving",
        "relationship": "Husband",
        "race": "Amer-Indian-Eskimo",
        "sex": "Male",
        "hoursPerWeek": 45,
        "nativeCountry": "Mexico"
    })
    assert r.status_code == 200
    assert r.json()['prediction'] == "<=50K"
