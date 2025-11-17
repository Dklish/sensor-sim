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
        self.voltage = round(random.uniform(10.0,12.0), 3)
        #initialize at room temp
        self.temp = round(20.0, 3)
        self.start_time = time.time()
        self.elapsed_time = 0
        #default state idle
        self.state = 1
        #creating object so we can poll continously from user
        self.poller = select.poll()
        self.poller.register(sys.stdin.fileno(), select.POLLIN)
        self.user_input = ""
        #self.values = [0,1,2]

    #function to access the private values
    def get_values(self):
        return self.voltage, self.temp

    def state_machine_running(self):
        if self.state == 2:
            logging.debug("Sensor is Running")
            self.temp += random.uniform(.1, .3)
            self.voltage = random.uniform(10, 12)
            self.elapsed_time = round(time.time() - self.start_time, 3)
            #I think this should return the time since the machine has been running initial time minus current
            print("Temp(C):", round(self.temp, 3), "Voltage(V):", round(self.voltage, 3), "Time(s):", self.elapsed_time)
            time.sleep(1)
            return

    def state_machine_idle(self):
        if self.state == 1:
            logging.debug("sensor is Idle")
            self.elapsed_time = round(time.time() - self.start_time, 3)
            print("Temp(C):", round(self.temp, 3), "Voltage(V):", round(self.voltage, 3), "Time(s):", self.elapsed_time)
            time.sleep(1)
            return

    def state_machine_off(self):
        if self.state == 0:
            self.voltage = 0
            self.temp -= round(random.uniform(.1, .5), 3)
            self.elapsed_time = 0
            logging.debug("Sensor is Off")
            print("Temp(C):", round(self.temp, 3), "Voltage(V):", round(self.voltage, 3), "Time(s):", self.elapsed_time)
            time.sleep(1)
            return

    def step(self):
        if self.state == 2:
            self.state_machine_running()
        elif self.state == 1:
            self.state_machine_idle()
        elif self.state == 0:
            self.state_machine_off()

        self.enforce_limits()


    #so our sensor does not get to hot or cool off into the abyss
    def enforce_limits(self):
        if self.temp >= 100:
            logging.warning("Overtemperature! Shutting sensor off.")
            self.state = 0
        if self.temp < 20.0 and self.state == 0:
            self.temp = 20.0

    def run_sensor(self):
        self.user_input = input("Enter s to turn sensor on!")
        if self.user_input == "s":
            print("enter q to quit sensor, 0 to turn if off, 2 to start it 1 to idle")
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
