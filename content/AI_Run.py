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
cam = cv2.VideoCapture(0)
########## Local import ###########
current_directory_path = os.path.abspath(os.path.join(__file__, "../../content"))
sys.path.insert(1, '{0}/yolov5'.format(current_directory_path))
import detect_custom




def image_capture():
    ret,frame = cam.read()
    cv2.imwrite("{0}/input.png".format(current_directory_path),frame)

def ai_capture():    
    global opt
    image_capture()
    opt = detect_custom.parse_opt()
    opt.source = "{0}/input.png".format(current_directory_path)
    opt.weights = "{0}/yolov5/runs/train/exp/weights/best.pt".format(current_directory_path)
    opt.imgsz = (640, 640)
    opt.conf_thres = 0.25
    opt.nosave = True
    opt.hide_conf = True
pass


# cmd = "python {0}/segment/predict.py --weights yolov5s-seg.pt --img 640 --conf 0.4 --source data/images".format(current_directory_path)
# cmd1 = "python {0}/yolov5/detect.py --source 0 --weights {0}/yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.25 --nosave --hide-conf".format(current_directory_path)   

                 

while True:
    # replace this with your logic to receive the signal from the server
    image_capture()
    ai_capture()
    detect_custom.reading_signal = detect_custom.reading_signal^1
    print(detect_custom.reading_signal)
    detect_custom.main(opt)
    time.sleep(10)


    