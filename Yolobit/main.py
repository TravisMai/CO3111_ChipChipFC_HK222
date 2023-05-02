print("Hello AIOT Python")
import sys
import paho.mqtt.client as mqtt
import time
import random
import os
# from uart import *
current_directory_path = os.path.abspath(os.path.join(__file__, "../../"))
print(current_directory_path)
sys.path.insert(1, '{0}'.format(current_directory_path))
from content import AI_Run

AIO_FEED_ID = ["nutnhan1", "nutnhan2", "signal"]
AIO_USERNAME = "EmChes"
AIO_KEY = "aio_jwjT59maC5PDDYyK5tgy3GOrnBjy"
ADA_TOPIC = [AIO_USERNAME + "/feeds/" +  ids for ids in AIO_FEED_ID]
ADA_SERVER = "io.adafruit.com"

MQTT_PORT = 1883

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)
   
def aiot_connected(client, userdata, flags, rc):
    print("Ket noi thanh cong ...")
    for id in ADA_TOPIC:
        client.subscribe(id)
        
def aiot_message(client , feed_id , payload):
    msg = payload.payload.decode('UTF-8')
    print("Data is from: " + payload.topic + ", Payload: " + msg)
    # uart_write(msg)

adaClient = mqtt.Client()
adaClient.username_pw_set(AIO_USERNAME, AIO_KEY)
adaClient.connect(ADA_SERVER, int(MQTT_PORT), 60)

adaClient.on_connect = aiot_connected
adaClient.on_subscribe = mqtt_subscribed
adaClient.on_message = aiot_message

adaClient.loop_start()

counter = 0

counter_sensor = 20
counter_ai = 10
counter_connect = 10
while True:
    time.sleep(1)
    # readSerial()            
    counter_sensor = counter_sensor - 1
    if counter_sensor <=0:
        counter_sensor = 20
        lux = random.randint(1,99)
        # lux = getLux()
        print(lux)
        adaClient.publish("EmChes/feeds/cambien3",lux)
    if counter_sensor == 15:
        humi = random.randint(1,99)
        # humi = getHumi()
        adaClient.publish("EmChes/feeds/cambien2",humi)
    if counter_sensor == 10:
        temp = random.randint(1,99)
        # temp = getTemp()
        adaClient.publish("EmChes/feeds/cambien1",temp)
        
    counter_ai = counter_ai - 1
    if counter_ai <=0:
        counter_ai = 15
        # AI_Run.image_capture()
        ai_result, image = AI_Run.ai_capture()
        # if ai_result == "yes mask": lmeo = 1
        # else: lmeo = 0
        adaClient.publish("EmChes/feeds/AI", ai_result)
        adaClient.publish("EmChes/feeds/image", image)