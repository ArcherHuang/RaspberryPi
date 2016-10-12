# **************************************************************************************************************************
# Version:     2016.10.12                                                                                                  #
# Author:      Archer Huang                                                                                                #
# License:     MIT                                                                                                         #
# Description: Raspberry Pi + Send Data To Google Firebase                                                                 #
# **************************************************************************************************************************

#**************************************************** 
# Import Package                                                                           
#**************************************************** 

import time   
import requests  
import json
import datetime
import sys  
sys.path.append('/home/pi/rpi/code/Package')  
import grovepi  
from grove_rgb_lcd import *

#**************************************************** 
# Set Firebase URL, Location, Pin No                                                   
#**************************************************** 

sensor = 4  
blue = 0    # The Blue colored sensor.  
white = 1   # The White colored sensor.

firebase_url = 'https://temperaturehumidity.firebaseio.com/'  
temperature_location = 'Taipei';  

while True:  
	[temperature,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temperature, humidity))
	setText("temp = %.02f C \nhumidity =%.02f%%"%(temperature, humidity))
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')

	#**************************************************** 
	# Insert Data                                                                              
	#**************************************************** 

	data = {'date':date,'temperature':temperature,'humidity':humidity}  
	result = requests.post(firebase_url + '/' + temperature_location + '/temperaturehumidity.json', data=json.dumps(data))  
	print 'Status Code = ' + str(result.status_code) + ', Response = ' + result.text
	time.sleep(1);
