# # -*- coding: utf-8 -*-

import sys

import paho.mqtt.client as paho
import json


THINGSBOARD_HOST = '172.16.206.223'
ACCESS_TOKEN = '5fCX5oI4LncCpngaogOy'

payload="{\"Humidity\":60,\"Temperature\":25}"
sensor_data = {'temperature': 777, 'humidity': 777}
# Write row to storage
client = paho.Client()
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, keepalive=60)
# Sending humidity and temperature data to ThingsBoard
client.publish("v1/devices/me/telemetry", json.dumps(sensor_data), 1)
#client.loop(2)


# # -*- coding: utf-8 -*-
# import paho.mqtt.client as mqtt

# mqttc = mqtt.Client("python_pub")
# #mqttc.username_pw_set("psd:vwcm","vwcm")
# mqttc.connect("52.67.34.106", 1883)
# mqttc.publish("teste", "Hello, World!")
# mqttc.loop(2) #timeout = 2s

# import paho.mqtt.client as paho  		    #mqtt library
# import os
# import json
# import time
# from datetime import datetime

# ACCESS_TOKEN='NN7QEiWaX6mxPRnVdJsQ'                 #Token of your device
# broker="demo.thingsboard.io"   			    #host name
# port=1883 					    #data listening port

# def on_publish(client,userdata,result):             #create function for callback
#     print("data published to thingsboard \n")
#     pass
# client1= paho.Client("control1")                    #create client object
# client1.on_publish = on_publish                     #assign function to callback
# client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
# client1.connect(broker,port,keepalive=60)           #establish connection

# while True:
  
#    payload="{"
#    payload+="\"Humidity\":60,"; 
#    payload+="\"Temperature\":25"; 
#    payload+="}"
#    ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
#    print("Please check LATEST TELEMETRY field of your device")
#    print(payload);
#    time.sleep(5)
