__author__ = 'uhs374h'
from threading import Thread
import time
import random
from observer.Subject import Subject


class WeatherData(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 30
        t = Thread(target=self.sensorLoop)
        t.start()

    def getState(self):
        """ Gets the observable state

        :return: the observable state
        """
        return self.temperature

    def sensorLoop(self):
        while True:
            time.sleep(1)
            delta = random.randint(1,200)/200-0.5
            self.temperature += delta
            self.notifyObservers()
            print(self.temperature)

