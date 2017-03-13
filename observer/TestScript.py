from observer.ConsoleObserver import ConsoleObserver
from observer.WeatherData import WeatherData
import time


if __name__ == "__main__":
    w = WeatherData()
    c1 = ConsoleObserver("1", w)
    c2 = ConsoleObserver("2", w)
    time.sleep(5)
    w.unregister(c1)