from fastapi.testclient import TestClient
from app.main import first_app, sensor

client = TestClient(first_app)


def test_read_sensor_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "temperature" in data
    assert "voltage" in data
    assert "state" in data
    assert "elapsed_time" in data

def test_change_state_and_step():
    # change to running
    resp = client.put("/sensor/state/2")
    assert resp.status_code == 200
    assert resp.json()["State"] == 2

    # step a few times
    resp = client.put("/sensor/step/3")
    assert resp.status_code == 200
    data = resp.json()
    assert "temperature" in data
    assert "voltage" in data
    assert data["state"] in [0, 1, 2]

def test_log_and_history_endpoints():
    # log current reading
    resp = client.post("/sensor/log")
    assert resp.status_code == 200

    # fetch history
    resp = client.get("/sensor/history?limit=5")
    assert resp.status_code == 200
    data = resp.json()
    assert "readings" in data
    assert len(data["readings"]) >= 1