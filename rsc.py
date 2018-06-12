from __future__ import print_function
import threading
import time, sys, atexit, socket, struct
from upm import pyupm_rsc as rsc
from functools import reduce

# For transfering data to server
class DataTransfer:
      
    TCP_IP = '192.168.3.1'
    TCP_PORT = 5005
      
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.TCP_IP,self.TCP_PORT))
        
    def __enter__(self):
        return self
        
    def sendData(self,tag, value):
        self.sock.send(tag.encode())
        packer = struct.Struct('f')
        packed_data = packer.pack(value)
        self.sock.send(packed_data)
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.sock.close()

# For storing and averagin pressure data
class RscDataHandler:
    
    INH2O_PASCAL = 248.84
    DEGC_KELVIN = 273.15
    
    def __init__(self, period):
        self.__pres__ = []
        self.__temp__ = []
        self.len = 0
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
            self.len = self.len + 1
            time.sleep(0.01)
            #print("Got " + str(self.len) + " samples")

    def __ave__(self,chan):
        if chan:
            return reduce(lambda x, y: x+y, self.__temp__)/float(self.len)
        else:
            return reduce(lambda x, y: x+y, self.__pres__)/float(self.len)
    
    def __clear__(self):
        del self.__pres__[:]
        del self.__temp__[:]
        self.len = 0

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


def main():

    # This function lets you run code on exit
    def exitHandler():
        print("Exiting")
        sys.exit(0)
    atexit.register(exitHandler)
    
    # Create the data handler, and transferer, then send data!
    dataHandler = RscDataHandler(0.5)
    dataTrans = DataTransfer()
    while True:
        if (not dataHandler.dataReady) and (not dataHandler.running):
            dataHandler.start()
        elif dataHandler.dataReady:
            print("Data ready, collected " + str(dataHandler.len) + " samples")
            pres, temp = dataHandler.getData()
            dataTrans.sendData("MWTP",pres)
            dataTrans.sendData("MWTT",temp)
        

if __name__ == '__main__':
    main()
