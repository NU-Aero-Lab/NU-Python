import socket
import struct
import time

TCP_IP = '192.168.3.1'
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
s.send("MWTV")
packer = struct.Struct('f')
packed_data = packer.pack(20.123)
s.send(packed_data)
print "Sent message 1"

time.sleep(10)

s.send("MWTV")
packer = struct.Struct('f')
packed_data = packer.pack(25.321)
s.send(packed_data)
print "Sent message 2"

time.sleep(10)

print "Closing connection"

s.close()
