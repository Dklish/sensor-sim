import random
import time
import logging
import select
import sys

logging.basicConfig(level=logging.DEBUG)

class Sensor:
    #initialize all values
    def __init__(self):
        #we want voltage, temp randomly initated in these ranges and then start time and state
        self.voltage = random.uniform(10.0,12.0)
        self.temp = random.uniform(20.0,40.0)
        self.start_time = time.time()
        self.elapsed_time = 0
        #default state idle
        self.state = 1
        #creating object so we can poll continously from user
        self.poller = select.poll()
        self.poller.register(sys.stdin.fileno(), select.POLLIN)
        #self.values = [0,1,2]



    #function to access the private values
    def get_values(self):
        return self.voltage, self.temp

    def state_machine_running(self):
        if self.state == 2:
            logging.debug("Sensor is Running")
            self.temp = random.uniform(20,100)
            self.voltage = random.uniform(10, 12)
            #I think this should return the time since the machine has been running initial time minus current
            self.elapsed_time = time.time() - self.start_time
            print("Temp(C): ", self.temp, "Voltage(V): ", self.voltage, "Time(s): ", self.elapsed_time)
            time.sleep(2)
            return

    def state_machine_idle(self):
        if self.state == 1:
            logging.debug("sensor is Idle")
            print("Temp(C): ", self.temp, "Voltage(V): ", self.voltage, "Time(s): ", self.elapsed_time)
            time.sleep(2)
            return

    def state_machine_off(self):
        if self.state == 0:
            self.voltage = 0.0
            self.temp = 0.0
            self.elapsed_time = 0
            logging.debug("Sensor is Off")
            print("Temp(C): ", self.temp, "Voltage(V): ", self.voltage, "Time(s): ", self.elapsed_time)
            time.sleep(2)
            return

    def step(self):
        if self.state == 2:
            self.state_machine_running()
        elif self.state == 1:
            self.state_machine_idle()
        elif self.state == 0:
            self.state_machine_off()

    def run_sensor(self):
        while True:
            self.step()
            time.sleep(.2)

            #poll for user input
            events = self.poller.poll(0)
            #if user typed something
            if events:
                user_input = sys.stdin.readline().strip()
                if user_input == "q":
                    print("Quitting Sensor loop")
                    break
                if user_input in ["0", "1", "2"]:
                    self.state = int(user_input)
                else:
                    logging.error("Invalid Input")

#create a object of sensor class type
sensor_1 = Sensor()
#okay here we are trying to run it
sensor_1.run_sensor()
