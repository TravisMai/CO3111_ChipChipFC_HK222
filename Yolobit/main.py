print("Hello IoT Python")
import sys
from Adafruit_IO import MQTTClient
import time
import os
# from simple_ai import *
from uart import *
hostname = "google.com"

AIO_FEED_ID = ["nutnhan1", "nutnhan2", "signal"]
AIO_USERNAME = "EmChes"
AIO_KEY = "aio_uQEH965f9YkdGRzsElbmRiGS8zJ9"

def connected(client):
    print("Ket noi thanh cong ...")
    client.publish("signal", "1")
    for id in AIO_FEED_ID:
        client.subscribe(id)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Data is from: " + feed_id + ", Payload: " + payload)
    if (feed_id == "signal"):
        if (payload=="0"):
            client.publish("signal", "1")
    else:        
        uart_write(payload)

lmeo = 0;
client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter_sensor = 30
counter_ai = 10
counter_connect = 10
while True:
    if (os.system("ping -n 1 " + hostname) == False):
        time.sleep(1)
        readSerial()            
        counter_sensor = counter_sensor - 1
        if counter_sensor <=0:
            counter_sensor = 30
            lux = getLux()
            client.publish("cambien3", lux)
        if counter_sensor == 20:
            humi = getHumi()
            client.publish("cambien2", humi)
        if counter_sensor == 10:
            temp = getTemp()
            client.publish("cambien1", temp)
    else:
        client.connect()
        time.sleep(10)

    # counter_ai = counter_ai - 1
    # if counter_ai <=0:
    #     counter_ai = 15
    #     image_capture()
    #     ai_result = image_detector()
    #     client.publish("AI", ai_result)

    pass
