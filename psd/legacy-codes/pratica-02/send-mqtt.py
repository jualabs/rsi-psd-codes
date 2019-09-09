# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client()
mqttc.username_pw_set("CAtKHB10EgI0xLSfAXAj")
mqttc.connect("localhost", 1883)
#mqttc.loop_start()
i = 0
while i < 100:
    time.sleep(1)
    mqttc.publish("v1/devices/me/telemetry", '{"key1":"value--", "key2":"value--"}')
    i = i + 1
#mqttc.loop_stop()

# import paho.mqtt.client as paho  		    #mqtt library
# import os
# import json
# import time
# from datetime import datetime

# ACCESS_TOKEN='CAtKHB10EgI0xLSfAXAj'                 #Token of your device
# broker='172.16.206.43'   			    #host name
# port=1883 					    #data listening port

# def on_publish(client,userdata,result):             #create function for callback
#     print("data published to thingsboard \n")
#     pass
# client1= paho.Client("control1")                    #create client object
# client1.on_publish = on_publish                     #assign function to callback
# client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
# client1.connect(broker,port,keepalive=60)           #establish connection
# client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device

# while True:
  
#    payload="{"
#    payload+="\"Humidity\":60,"; 
#    payload+="\"Temperature\":25"; 
#    payload+="}"
#    ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
#    print("Please check LATEST TELEMETRY field of your device")
#    print(payload);
#    time.sleep(5)

