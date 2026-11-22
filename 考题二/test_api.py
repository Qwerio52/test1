from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_record_success():
    resp = client.post("/records", json={
        "amount": 100,
        "rtype": "收入",
        "category": "兼职",
        "record_date": "2026-11-18"
    })
    assert resp.status_code == 200
    assert resp.json()["msg"] == "添加成功"

def test_add_record_wrong_type():
    resp = client.post("/records", json={
        "amount": 50,
        "rtype": "转账",
        "category": "测试",
        "record_date": "2026-11-18"
    })
    assert resp.status_code == 400

def test_add_record_negative_amount():
    resp = client.post("/records", json={
        "amount": -10,
        "rtype": "支出",
        "category": "吃饭",
        "record_date": "2026-11-18"
    })
    assert resp.status_code == 400

def test_add_record_bad_date():
    resp = client.post("/records", json={
        "amount": 20,
        "rtype": "支出",
        "category": "奶茶",
        "record_date": "2026/11/18"
    })
    assert resp.status_code == 400

def test_get_records():
    resp = client.get("/records")
    assert resp.status_code == 200
    assert "data" in resp.json()

def test_summary():
    resp = client.get("/summary", params={"start_date":"2026-11-01", "end_date":"2026-11-30"})
    assert resp.status_code == 200
    assert "收入合计" in resp.json()