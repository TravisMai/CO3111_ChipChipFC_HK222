######### Library import #########
import os
import sys
from PIL import Image, ImageOps
import numpy as np
import cv2
import time
import multiprocessing
import threading
import signal
########## Local import ##########
current_directory_path = os.path.abspath(os.path.join(__file__, "..\..\content"))
sys.path.insert(1, '{0}/yolov5'.format(current_directory_path))
import detect_custom


opt = detect_custom.parse_opt()
opt.source = "0"
opt.weights = "{0}/yolov5/runs/train/exp/weights/best.pt".format(current_directory_path)
opt.imgsz = (640, 640)
opt.conf_thres = 0.25
opt.nosave = True
opt.hide_conf = True
detect_custom.main(opt)

def ai_capture():
    # os.system(cmd)
    pass

print('__file__:    ', current_directory_path)
cmd = "python {0}\yolov5/detect.py --source 0 --weights {0}/yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.25 --nosave --hide-conf".format(current_directory_path)   



signal = 0
t1 = threading.Timer(0, ai_capture)


def handle_signal(sig):
    global signal, t1
    if sig == 1 and not t1.is_alive():
        t1.start()
    elif sig == 0 and t1.is_alive():
        signal = 0
        cv2.destroyAllWindows()
                   

while True:
    # replace this with your logic to receive the signal from the server
    signal = signal^1
    print(signal)
    handle_signal(signal)
    time.sleep(10)


    