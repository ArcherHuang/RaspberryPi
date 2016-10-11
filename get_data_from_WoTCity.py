# ********************************************************************************************
# Version:     2016.10.12                                                                    #
# Author:      Archer Huang                                                                  #
# License:     MIT                                                                           #
# Description: Get Data From WoT.City                                                        #
# ********************************************************************************************

import websocket

websocket.enableTrace(True)
ws = websocket.create_connection("ws://wot.city/object/57cad2809453b2446f0007de/viewer")

while True:
	result = ws.recv()
	print "Received '%s'" % result