# **************************************************************************************************************************
# Version:     2016.10.16                                                                                                  #
# Author:      Archer Huang                                                                                                #
# License:     MIT                                                                                                         #
# Description: Raspberry Pi + Send Data To IBM Bluemix Publish                                                             #
# **************************************************************************************************************************

#**************************************************** 
# Import Package                                                                           
#**************************************************** 

import time  
import sys  
import ibmiotf.application  
import ibmiotf.device  
import json
sys.path.append('/home/pi/rpi/code/Package')  
import grovepi  
from grove_rgb_lcd import *

#**************************************************** 
# Set IBM Bluemix Config, Pin No                                                   
#**************************************************** 

sensor = 4  
blue = 0    # The Blue colored sensor.  
white = 1   # The White colored sensor.

deviceOptions = {  
  "org": "組織 ID",
  "type": "裝置類型",
  "id": "裝置 ID",
  "auth-method": "token",
  "auth-token": "鑑別記號"
}

#**************************************************** 
# Set IBM Bluemix Connection                                                   
#**************************************************** 

try:  
	deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:  
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

deviceCli.connect()

#**************************************************** 
# Publish Event To IBM Bluemix                                                   
#**************************************************** 

while True:  
	[temperature,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temperature, humidity))
	
	msg = json.JSONEncoder().encode({"d":{"Temperature":temperature, "Humidity":humidity}})
	print "send payload: " + msg
	deviceCli.publishEvent("TemperatureHumidity", "json", msg)
	time.sleep(1)
