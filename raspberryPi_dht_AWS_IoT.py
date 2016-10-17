# **************************************************************************************************************************
# Version:     2016.10.17                                                                                                  #
# Author:      Archer Huang                                                                                                #
# License:     MIT                                                                                                         #
# Description: Raspberry Pi + Send Data To AWS                                                                             #
# **************************************************************************************************************************

#**************************************************** 
# Import Package                                                                           
#**************************************************** 

import time
import datetime 
import paho.mqtt.client as paho 
import json
import ssl 
import sys
sys.path.append('/home/pi/rpi/code/Package')
import grovepi
from grove_rgb_lcd import *

#**************************************************** 
# Set Pin No, AWS Config                                                                          
#**************************************************** 

sensor = 4 
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

connflag = False

#**************************************************** 
# Set AWS Connection                                                   
#**************************************************** 

def on_connect(client, userdata, flags, rc):  
	global connflag
	connflag = True
	print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):  
	print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()  
mqttc.on_connect = on_connect  
mqttc.on_message = on_message

awshost = "a3iprlpgye4dmu.iot.us-west-2.amazonaws.com"  
awsport = 8883  
clientId = "sensorData"  
thingName = "sensorData"  
caPath = "./root-CA.crt"  
certPath = "./000cd28455-certificate.pem.crt"  
keyPath = "./000cd28455-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  
mqttc.connect(awshost, awsport, keepalive=60)  
mqttc.loop_start()

#**************************************************** 
# Publish AWS                                                  
#**************************************************** 

while True:
	[temp,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
	t = time.time();
	date = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d%H%M%S')
	if connflag == True:
		mqttc.publish("topic/sensorData", json.dumps({"time": date, "temperature": temp, "humidity": humidity}), qos=1)
	else:
		print("waiting for connection...")
	time.sleep(1)
