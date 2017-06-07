# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

mqttc = mqtt.Client("python_pub")
#mqttc.username_pw_set("psd:vwcm","vwcm")
mqttc.connect("52.67.34.106", 1883)
mqttc.publish("teste", "Hello, World!")
mqttc.loop(2) #timeout = 2s
