from envirophat import weather
from genericDataHandler import GenericDataHandler
from functools import reduce

class EnviroHatDataHandler(GenericDataHandler):

    def __init__(self, period):
        super().__init__(period, "EnviropHAT")
        self.__atm_pres__ = []
        self.__atm_temp__ = []

    def __append__(self):
        self.__atm_pres__.append(weather.pressure())
        self.__atm_temp__.append(weather.temperature()  + self.DEGC_KELVIN)
            
    def len(self):
        return len(self.__atm_pres__)

    def __ave__(self,chan):
        if chan:
            return reduce(lambda x, y: x+y, self.__atm_temp__)/float(len(self.__atm_temp__))
        else:
            return reduce(lambda x, y: x+y, self.__atm_pres__)/float(self.len())
    
    def __clear__(self):
        del self.__atm_pres__[:]
        del self.__atm_temp__[:]
        
    def __size__(self):
        return len(self.__atm_pres__)

