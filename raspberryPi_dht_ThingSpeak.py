# **************************************************************************************************************************
# Version:     2016.10.17                                                                                                  #
# Author:      Archer Huang                                                                                                #
# License:     MIT                                                                                                         #
# Description: Raspberry Pi + Send Data To ThingSpeak                                                                      #
# **************************************************************************************************************************

#**************************************************** 
# Import Package                                                                           
#**************************************************** 

import sys
import time  
import httplib, urllib
sys.path.append('/home/pi/rpi/code/Package')
import grovepi
from grove_rgb_lcd import *

#**************************************************** 
# Set Pin No, ThingSpeak Key                                                                          
#**************************************************** 

sensor = 4 
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

thingSpeakApiKey = "XDFR4PLTEFD2NEFL"

#**************************************************** 
# Set ThingSpeak Connection                                                   
#**************************************************** 

def post_to_thingspeak(payload):  
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	not_connected = 1
	while (not_connected):
		try:
			conn = httplib.HTTPConnection("api.thingspeak.com:80")
			conn.connect()
			not_connected = 0
		except (httplib.HTTPException, socket.error) as ex:
			print "Error: %s" % ex
			time.sleep(10)  # sleep 10 seconds

	conn.request("POST", "/update", payload, headers)
	response = conn.getresponse()
	print( response.status, response.reason, payload, time.strftime("%c"))
	data = response.read()
	conn.close()

#**************************************************** 
# Post ThingSpeak                                                  
#**************************************************** 

while True:
	[temp,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
	params = urllib.urlencode({'field1': temp, 'field2': humidity, 'key': thingSpeakApiKey})
	post_to_thingspeak(params)
	time.sleep(5)
