#!python3
from datetime import datetime
import subprocess
import time
import logging 

##########
#Startup
##########

print('Input target URL / IP!')
target=input()
print('Pinging to '+target)

##########
#setup logging
##########
logging.basicConfig(filename=target+'.log',format='%(asctime)s - %(message)s',level=logging.INFO)

##########
#Process reference
##########
#output = pingProc.stdout
#outErr = pingProc.stderr
#TraceRoute output
#tOutput = traceProc.stdout
#tOutErr = traceProc.stderr

#print(output,outErr)
#print(tOutput,tOutErr)

##########
#The Loop!
##########

currentTime=datetime.now().hour
print('Hour:',currentTime)

while True:
    
    time.sleep(1)
    
    if currentTime != datetime.now().hour:
        currentTime=datetime.now().hour
        print('\nHour:',currentTime)

    pingProc = subprocess.run(["ping",target,"-n","1"],encoding='utf-8',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    
    if 'Request timed out.' in pingProc.stdout:
        logging.warning('Ping to '+target+' failed!')
        print('!',flush=True, end="")
        #traceProc = subprocess.run(["tracert",target],encoding='utf-8',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #logging.warning(traceProc.stdout)
        #print('!')
    
    else:
        print('.',flush=True, end="")
        time.sleep(3)
        #print('.')