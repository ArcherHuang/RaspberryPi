# **************************************************************************************************************************
# Version:     2016.10.12                                                                                                  #
# Author:      Archer Huang                                                                                                #
# License:     MIT                                                                                                         #
# Description: Raspberry Pi + Send Data To WoT.City                                                                        #
# **************************************************************************************************************************
# 
# 1. install setuptools
#	 curl https://bootstrap.pypa.io/ez_setup.py -k -o - | python
#
# 2. install six
# 	 wget --no-check-certificate https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz
# 	 tar zxvf six-1.10.0.tar.gz
#	 cd six-1.10.0
#	 python setup.py install
#
# 3. install Websocket
#	 wget --no-check-certificate https://pypi.python.org/packages/source/w/websocket-client/websocket_client-0.32.0.tar.gz
#	 tar zxvf websocket_client-0.32.0.tar.gz
#	 cd websocket_client-0.32.0
#	 python setup.py install
# 
# Dashboard
# 	http://52.42.77.220/dashboard2/index.html#57615d8a54242e1f2a000ee5
# **************************************************************************************************************************

import time   
import websocket  
import datetime
import sys  
sys.path.append('/home/pi/rpi/code/Package')  
import grovepi  
from grove_rgb_lcd import *

sensor = 4  
blue = 0    # The Blue colored sensor.  
white = 1   # The White colored sensor.

websocket.enableTrace(True)  
ws = websocket.create_connection("ws://wot.city/object/57cad2809453b2446f0007de/send")

while True:  
	[temp,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
	setText("temp = %.02f C \nhumidity =%.02f%%"%(temp, humidity))
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	vals = "{\"date\":\""+date+"\",\"temperature\":"+str(temp)+",\"h\":"+str(humidity)+"}"
	time.sleep(1);
	ws.send(vals);
	print vals;
