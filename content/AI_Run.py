import os
from PIL import Image, ImageOps
import numpy as np
import cv2
import time



cam = cv2.VideoCapture(0)
current_directory_path = os.path.abspath(os.path.join(__file__, "..\..\content"))
def image_capture():
    ret,frame = cam.read()
    cv2.imwrite("{0}\input.png".format(current_directory_path),frame)


print('__file__:    ', current_directory_path)
cmd = "python {0}\yolov5/detect.py --source {0}\input.png --weights {0}\yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.25 --nosave".format(current_directory_path)   

for num in range(1, 11):
    image_capture()
    os.system(cmd)
    