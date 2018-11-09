import threading

class GenericDataHandler(object):

    DEGC_KELVIN = 273.15

    def __init__(self, period, name):
        self.period = period
        self.running = False
        self.dataReady = False
        self.name = name

    def __setReady__(self):
        self.running = False
        self.dataReady = True

    def start(self):
        if not self.dataReady:
            self.__clear__()
            threading.Thread(target = self.collect).start() # Use a thread to do this in parrallel
            threading.Timer(self.period,self.__setReady__).start() # Stop collecting data and set sensor to ready after "period" seconds

    def collect(self):
        self.running = True
        while self.running:
            self.__append__()

    def getData(self):
        self.dataReady = False
        return (self.__ave__(0),self.__ave__(1))

    def print(self):
        pass

    def __append__(self):
        pass

    def __clear__(self):
        pass

    def __ave__(self,chan):
        pass
    
    def size(self):
        pass
    
    def stdev(self):
        pass
    
    def min(self):
        pass
    
    def max(self):
        pass
