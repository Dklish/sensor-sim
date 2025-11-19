from fastapi import FastAPI
from sensor_sim.sensor import Sensor

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


