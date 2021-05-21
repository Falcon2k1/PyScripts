#!python3
from ping3 import ping, verbose_ping
from datetime import datetime
import time
import logging 

logging.basicConfig(filename='ping.log',format='%(asctime)s - %(message)s',level=logging.INFO)

print('Input target URL / IP!')
target=input()
print('Pinging to '+target)

currentTime=datetime.now().hour
print('Hour:',currentTime,"|", flush=True, end="")
while True:
    time.sleep(1)
    if currentTime != datetime.now().hour:
        currentTime=datetime.now().hour
        print('\nHour:',currentTime,"|")
    if ping(target) == None:
        logging.warning('Ping to '+target+' failed!')
        print('!',flush=True, end="")
        #print('!')
    else:
        print('.',flush=True, end="")
        time.sleep(3)
        #print('.')

