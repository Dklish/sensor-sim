from fastapi import FastAPI
from sensor_sim.sensor import Sensor

#create our app
first_app = FastAPI()

#create our sensor object
sensor = Sensor()

#where we will store our sensor readings in the future
Sensor_data = []

@first_app.get("/")
def read_sensor():
    temp, voltage = sensor.get_values()
    return{
        "temperature": temp,
        "voltage": voltage,
        "state": sensor.state,
    }
