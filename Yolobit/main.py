print("Hello AIOT Python")
import sys
import paho.mqtt.client as mqtt
import time
import os
from uart import *
hostname = "google.com"

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "ohshift"
MQTT_PASSWORD = ""
MQTT_TOPIC = ["V1","V2","V3","V4","V5","V6","V7",]
# MQTT_TOPIC_PUB_NAME = "SmartBin2907123/feeds/V17"
# MQTT_TOPIC_PUB_INDEX = "SmartBin2907123/feeds/V16"

def mqtt_connected(client, userdata, flags, rc):
    print("Ket noi thanh cong ...")
    for id in MQTT_TOPIC:
        client.subscribe(id)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)
    
mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed

mqttClient.loop_start()
counter = 0

counter_sensor = 30
counter_ai = 10
counter_connect = 10
while True:
    if (os.system("ping -n 1 " + hostname) == False):
        time.sleep(1)
        readSerial()            
        counter_sensor = counter_sensor - 1
        if counter_sensor <=0:
            counter_sensor = 20
            lux = getLux()
            mqttClient.publish("V5", lux)
        if counter_sensor == 15:
            humi = getHumi()
            mqttClient.publish("V4", humi)
        if counter_sensor == 10:
            temp = getTemp()
            mqttClient.publish("V3", temp)
        if counter_sensor == 5:
            sm = getSm()
            mqttClient.publish("V6", sm)
    else:
        mqttClient.connect()
        time.sleep(10)
        
    pass

# def connected(client):
#     print("Ket noi thanh cong ...")
#     client.publish("signal", "1")
#     for id in AIO_FEED_ID:
#         client.subscribe(id)

# def subscribe(client , userdata , mid , granted_qos):
#     print("Subscribe thanh cong ...")

# def disconnected(client):
#     print("Ngat ket noi ...")
#     sys.exit (1)

# def message(client , feed_id , payload):
#     print("Data is from: " + feed_id + ", Payload: " + payload)
#     if (feed_id == "signal"):
#         if (payload=="0"):
#             client.publish("signal", "1")
#     else:        
#         uart_write(payload)

# lmeo = 0;
# client = MQTTClient(AIO_USERNAME , AIO_KEY)
# client.on_connect = connected
# client.on_disconnect = disconnected
# client.on_message = message
# client.on_subscribe = subscribe
# client.connect()
# client.loop_background()
# counter_sensor = 30
# counter_ai = 10
# counter_connect = 10
# while True:
#     if (os.system("ping -n 1 " + hostname) == False):
#         time.sleep(1)
#         readSerial()            
#         counter_sensor = counter_sensor - 1
#         if counter_sensor <=0:
#             counter_sensor = 30
#             lux = getLux()
#             client.publish("cambien3", lux)
#         if counter_sensor == 20:
#             humi = getHumi()
#             client.publish("cambien2", humi)
#         if counter_sensor == 10:
#             temp = getTemp()
#             client.publish("cambien1", temp)
#     else:
#         client.connect()
#         time.sleep(10)
        
#     pass
