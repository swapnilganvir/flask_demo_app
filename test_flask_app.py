import pytest
import json

# import flask instance 'app' from file app.py
from app import app

# we want to reuse the client, so we use fixtures
@pytest.fixture # decorator over a function
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get('/ping')
    assert resp.status_code == 200
    assert resp.json == {"message": "Hi there, I'm working!!"}

def test_predict(client):
    test_data = {
        "Gender":"Male", 
        "Married":"Unmarried",
        "Credit_History" : "Unclear Debts",
        "ApplicantIncome":100000,
        "LoanAmount":2000000
    }
    resp = client.post('/predict', json=test_data)
    assert resp.status_code == 200
    assert resp.json == {'loan_approval_status': 'Rejected'}
    # assert resp.json == {'loan_approval_status': 'Accepted'}

