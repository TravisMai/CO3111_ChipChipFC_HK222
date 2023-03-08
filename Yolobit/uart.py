print("Hello Sensors")
from tempfile import tempdir
import serial.tools.list_ports
import time



def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "USB-SERIAL" in strPort:
            splitPort = strPort.split(" ")
            commPort = (splitPort[0])
    return commPort
mess = ""
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    global splitData
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "RT":
        global temperature
        temperature = splitData[2]
    if splitData[1] == "RH":
        global humidity
        humidity = splitData[2]
    if splitData[1] == "LUX":
        global luxury
        luxury = splitData[2]

def getTemp():
    return temperature

def getHumi():
    return humidity

def getLux():
    return luxury

def uart_write(data):
    ser.write((str(data) ).encode())
    return

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        # print("lmeolmeo lmeo")
        # print(mess)
        while ("#" in mess) and ("!" in mess):
            
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]
        print("\n")

portName = getPort()

if portName != "None":
    ser = serial.Serial(port=portName, baudrate=115200)

print(ser)

# while True:
#     readSerial()
#     time.sleep(0.5)