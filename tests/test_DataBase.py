from sensor_sim import DataBase

#unit test for database

def test_db_init_and_log_and_history(tmp_path, monkeypatch):
    # Redirect DB_PATH to a temporary file for this test run
    test_db_path = tmp_path / "test_sensor_data.db"
    monkeypatch.setattr(DataBase, "DB_PATH", test_db_path)

    # Now all DB functions will use the temp file
    DataBase.init_db()

    # Log one reading
    DataBase.log_reading(25.0, 11.5, 2)

    # Retrieve history
    rows = DataBase.get_history(limit=10)
    assert len(rows) == 1

    ts, temp, volt, state = rows[0]
    assert isinstance(ts, float)
    assert temp == 25.0
    assert volt == 11.5
    assert state == 2
