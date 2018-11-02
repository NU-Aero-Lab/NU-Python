import time, sys, atexit, socket, struct

# For transfering data to server
class DataTransfer:
      
    TCP_IP = '192.168.1.100'
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
