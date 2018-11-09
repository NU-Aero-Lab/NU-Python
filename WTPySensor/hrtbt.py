import time
from genericDataHandler import GenericDataHandler
#For checking if data is being recieved by the user
class HeartBeat(GenericDataHandler):
        
        def __init__(self, period):
            super().__init__(period, "Heartbeat")
            self.hb = 0

        def beat(self):
            self.dataReady = False
            if self.hb:
                self.hb = 0
            else:
                self.hb = 1
            return float(self.hb)