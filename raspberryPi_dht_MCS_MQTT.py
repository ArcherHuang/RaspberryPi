import paho.mqtt.client as mqtt
import json
import sys
sys.path.append('/home/pi/rpi/code/Package')
import grovepi
from grove_rgb_lcd import *

sensor = 4 
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

deviceId = "D2WKWKcr"  
deviceKey = "LcWuC5DykgbM5fqS"  
dataChnId1 = "Humidity"  
dataChnId2 = "Temperature"  
MQTT_SERVER = "mqtt.mcs.mediatek.com"  
MQTT_PORT = 1883  
MQTT_ALIVE = 60  
MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId1  
MQTT_TOPIC1 = "mcs/" + deviceId + "/" + deviceKey + "/" + dataChnId2

mqtt_client = mqtt.Client()  
mqtt_client.connect(MQTT_SERVER, MQTT_PORT, MQTT_ALIVE) 

while True:
	[temp,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
	payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":humidity}}]}
	mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
	payload = {"datapoints":[{"dataChnId":"Temperature","values":{"value":temp}}]}
	mqtt_client.publish(MQTT_TOPIC1, json.dumps(payload), qos=1)
	time.sleep(1)
