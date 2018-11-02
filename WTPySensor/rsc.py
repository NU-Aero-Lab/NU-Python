import time, sys, atexit
from upm import pyupm_rsc as rsc
from functools import reduce
from genericDataHandler import GenericDataHandler

# For storing and averagin pressure data
class RscDataHandler(GenericDataHandler):
    
    INH2O_PASCAL = 248.84
    # OFFSET = -19.558 
    def __init__(self, period):
        super().__init__(period)
        self.__pres__ = []
        self.__temp__ = []
        self.sensor = rsc.RSC(0, 11, 12)

        print("Sensor Name: {0}".format(self.sensor.getSensorName()))
        print("Sensor Serial Number: {0}".format(self.sensor.getSensorSerialNumber()))

    def __append__(self):
        self.__pres__.append(self.sensor.getPressure()*self.INH2O_PASCAL + self.OFFSET)
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



