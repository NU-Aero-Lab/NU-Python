import time, sys, atexit, statistics, math
from upm import pyupm_rsc as rsc
from functools import reduce
from genericDataHandler import GenericDataHandler

# For storing and averagin pressure data
class RscDataHandler(GenericDataHandler):
    
    INH2O_PASCAL = 248.84
    # OFFSET = -19.558 
    def __init__(self, period):
        super().__init__(period, "RSC")
        self.__pres__ = []
        self.__temp__ = []
        self.sensor = rsc.RSC(2, 11, 12)
        self.sensor.setDataRate(14)
        self.sensor.setMode(2)

        print("Sensor Name: {0}".format(self.sensor.getSensorName()))
        print("Sensor Serial Number: {0}".format(self.sensor.getSensorSerialNumber()))

    def __append__(self):
        self.__pres__.append(self.sensor.getPressure()*self.INH2O_PASCAL)
        self.__temp__.append(self.sensor.getTemperature() + self.DEGC_KELVIN)
            
    def len(self):
        return len(self.__pres__)

    def __ave__(self,chan):
        if chan:
            return statistics.mean(self.__temp__)
        else:
            return statistics.mean(self.__pres__)
    
    def __clear__(self):
        del self.__pres__[:]
        del self.__temp__[:]
        
    def size(self):
        return len(self.__pres__)
    
    def print(self):
        for p in self.__pres__:
            print(p)
            
    def stdev(self):
        return statistics.stdev(self.__pres__)
    
    def min(self):
        return max(self.__pres__)
    
    def max(self):
        return min(self.__pres__)



