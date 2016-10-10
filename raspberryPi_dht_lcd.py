import sys
sys.path.append('/home/pi/rpi/code/Package')
import grovepi
from grove_rgb_lcd import *

sensor = 4 
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

while True:
	[temp,humidity] = grovepi.dht(sensor,blue)  
	print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))
	setText("temp = %.02f C \nhumidity =%.02f%%"%(temp, humidity))
