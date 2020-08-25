from network import Sigfox
import socket
from machine import Pin
from onewire import DS18X20
from onewire import OneWire
import time


# init Sigfox for RCZ1 (Europe)
sigfox = Sigfox(mode=Sigfox.SIGFOX, rcz=Sigfox.RCZ1)

# create a Sigfox socket
s = socket.socket(socket.AF_SIGFOX, socket.SOCK_RAW)

# make the socket blocking
s.setblocking(True)

# configure it as uplink only
s.setsockopt(socket.SOL_SIGFOX, socket.SO_RX, False)
#for cycles in range(10):
# send some bytes
#    s.send(bytes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
#   time.sleep(30)



# DS18B20 data line connected to pin P10
#ow = OneWire(Pin('P10'))
#temp = DS18X20(ow)




#while True:
#for cycles in range(10):
  #  tsense=DS18X20(Pin('G17', mode=Pin.OUT))
   # temp = int(round(tsense.read_temp()*100))
  #  print(temp)
   # messageBytes=bytes((temp & 0xff, ((temp >> 8) & 0xff)))
   # s.send(messageBytes)
   # time.sleep(10)


ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

while True:
    temp.start_conversion()
    tempSend=temp.read_temp_async()
    time.sleep(1)
    
    messageBytes=bytes((temp.read_temp_async() & 0xff, ((temp.read_temp_async() >> 8) & 0xff)))
    print(temp.read_temp_async())
    s.send(messageBytes)
    time.sleep(2)