from sensor_sim.sensor import Sensor
#unit test for sensor

#test sensor state
def test_sensor_initial_state():
    s = Sensor()
    assert s.state == 1  # idle
    temp, volt = s.get_values()
    assert 10.0 <= s.voltage <= 12.0
    assert 19.0 <= s.temp <= 21.0  # depending on your random range

def test_set_state_valid():
    s = Sensor()
    assert s.set_state(2) is True
    assert s.state == 2

def test_set_state_invalid():
    s = Sensor()
    old_state = s.state
    assert s.set_state(99) is False
    assert s.state == old_state

def test_enforce_limits_overtemp():
    s = Sensor()
    s.temp = 200.0
    s.state = 2
    s.enforce_limits()
    assert s.state == 0

def test_enforce_limits_lowtemp_floor():
    s = Sensor()
    s.state = 0
    s.temp = 10.0
    s.enforce_limits()
    assert s.temp == 20.0

