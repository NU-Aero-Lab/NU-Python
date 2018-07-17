import threading
import time, sys, atexit
from upm import pyupm_rsc as rsc
from functools import reduce

# For storing and averagin pressure data
class RscDataHandler:
    
    INH2O_PASCAL = 248.84
    DEGC_KELVIN = 273.15
    
    def __init__(self, period):
        self.__pres__ = []
        self.__temp__ = []
        self.running = False
        self.period = period
        self.sensor = rsc.RSC(0, 11, 12)
        self.dataReady = False

        print("Sensor Name: {0}".format(self.sensor.getSensorName()))
        print("Sensor Serial Number: {0}".format(self.sensor.getSensorSerialNumber()))
        
    def start(self):
        if not self.dataReady:
            self.__clear__()
            threading.Thread(target = self.collect).start()
            threading.Timer(self.period,self.__setReady__).start()

    def collect(self):
        self.running = True
        while self.running:
            self.__pres__.append(self.sensor.getPressure()*self.INH2O_PASCAL)
            self.__temp__.append(self.sensor.getTemperature() + self.DEGC_KELVIN)
            
    def len(self):
        return len(self.__pres__)

    def __ave__(self,chan):
        if chan:
            return reduce(lambda x, y: x+y, self.__temp__)/float(len(self.__temp__))
        else:
            return reduce(lambda x, y: x+y, self.__pres__)/float(self.len())
    
    def __clear__(self):
        del self.__pres__[:]
        del self.__temp__[:]

    def __setReady__(self):
        print("Getting data ready...")
        self.running = False
        self.dataReady = True
        
    def getData(self):
        [print("{0:0.1f}".format(p)) for p in self.__pres__]
        self.dataReady = False
        res = (self.__ave__(0),self.__ave__(1))
        print(res[0])
        return res

