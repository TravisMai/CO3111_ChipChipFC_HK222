import os
from PIL import Image, ImageOps
import numpy as np
import cv2
import time
import multiprocessing
import threading
import signal


cam = cv2.VideoCapture(0)
current_directory_path = os.path.abspath(os.path.join(__file__, "..\..\content"))

def ai_capture():
    os.system(cmd)

print('__file__:    ', current_directory_path)
cmd = "python {0}\yolov5/detect_custom.py --source 0 --weights {0}\yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.25 --nosave --hide-conf".format(current_directory_path)   



signal = 0
t1 = threading.Timer(0, ai_capture)



def handle_signal(sig):
    global signal, t1
    if sig == 1 and not t1.is_alive():
        t1.start()
    elif sig == 0:
        signal = 0
        t1.finished.set()

            

while True:
    # replace this with your logic to receive the signal from the server
    signal = signal^1
    print(signal)
    handle_signal(signal)
    time.sleep(10)
    t1.finished.set()


    