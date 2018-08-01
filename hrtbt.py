import time
from genericDataHandler import GenericDataHandler
#For checking if data is being recieved by the user
class HeartBeat(GenericDataHandler):
        
        def __init__(self, period):
                super().__init__(period)
                print("Beating")

        def beat (self):
                return 1
