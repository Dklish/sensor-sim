from fastapi import FastAPI
from sensor_sim.sensor import Sensor
from sensor_sim.DataBase import init_db, log_reading, get_history

#create our sensor data table
init_db()
#create our app
first_app = FastAPI()
#create our sensor object
sensor = Sensor()

#read from sensor
@first_app.get("/")
def read_sensor():
    temp, voltage = sensor.get_values()
    return{
        "temperature": temp,
        "voltage": voltage,
        "state": sensor.state,
        "elapsed_time": sensor.elapsed_time,
    }

#set sensor state
@first_app.put("/sensor/state/{val}")
def change_state(val:int):
    sensor.set_state(val)
    return {
        "State": sensor.state,
    }

#step through this many times at current state
@first_app.put("/sensor/step/{val}")
def step_sensor(val:int = 1):
    for _ in range(val):
        sensor.step()
    temp, voltage = sensor.get_values()
    return{
        "temperature": sensor.temp,
        "voltage": sensor.voltage,
        "state": sensor.state,
        "elapsed_time": sensor.elapsed_time,
    }

# log the current reading to the database
@first_app.post("/sensor/log")
def log_current_reading():
    temp, voltage = sensor.get_values()
    log_reading(temp, voltage, sensor.state)
    return {"status": "ok"}


# fetch last N logged readings
@first_app.get("/sensor/history")
def read_history(limit: int = 20):
    rows = get_history(limit)
    return {
        "readings": [
            {
                "timestamp": r[0],
                "temperature": r[1],
                "voltage": r[2],
                "state": r[3],
            }
            for r in rows
        ]
    }
