import random
import time
import logging as logger

class Sensor:
    #private values
    def _init_(self):
        #we want voltage, temp randomly initated in these ranges and then start time and state
        self.voltage = random.uniform(10.0,12.0)
        self.temp = random.uniform(20.0,40.0)
        self.start_time = time.time()
        self.elapsed_time = 0
        self.state = 0

    #function to access the private values
    def _get_values(self):
        return self.voltage, self.temp


    def state_machine_running(self):
        while self.state == 2:
            logger.debug("Sensor is Running")
            temp = random.uniform(20,100)
            voltage = random.uniform(10, 12)
            #I think this should return the time since the machine has been running initial time minus current
            elapsed_time = time.time() - start_time

    def state_machine_idle(self):
        while self.state == 1:
            logger.debug("sensor is Idle")
            return self.temp, self.voltage
            time.sleep(1)

    def state_machine_off(self):
        self.voltage = 0.0
        self.temp = 0.0
        self.elapsed_time = 0
        logger.debug("Sensor is Off")

    def set_state(self, val):
        while val < 2 or val > 0:
            self._init_()
            if val == 2:
                self.state_machine_running()
            elif val == 1:
                self.state_machine_idle()
            elif val == 0:
                self.state_machine_off()
            else:
                logger.error("State input is invalid")


#okay here we are trying to run it

sensor_1 = Sensor()
sensor_1.set_state(2)
time.sleep(10)
sensor_1.set_state(0)