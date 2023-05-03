######### Library import #########
import base64
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
    image = cv2.resize(frame,(250,180),interpolation=cv2.INTER_AREA)
    res, image = cv2.imencode('.png',image)
    data = base64.b64encode(image)
    return data

def image_transform():
    cv2.imwrite("{0}/input_detect.png".format(current_directory_path),detect_custom.annotate_image)
    compress_image = cv2.resize(detect_custom.annotate_image,(250,150),interpolation=cv2.INTER_AREA)
    res, compress_image = cv2.imencode('.png',compress_image)
    data = base64.b64encode(compress_image)
    return data

def ai_capture():    
    global opt
    image_capture()
    opt = detect_custom.parse_opt()
    opt.source = "{0}/input.png".format(current_directory_path)
    opt.weights = "{0}/yolov5/runs/train/exp/weights/best_tree.pt".format(current_directory_path)
    opt.imgsz = (224, 224)
    opt.conf_thres = 0.5
    opt.line_thickness = 1
    opt.exist_ok = True
    opt.name = "output.png"
    opt.project = "{0}/output".format(current_directory_path)
    detect_custom.main(opt)
    data = image_transform()

    return detect_custom.publish_result, data
pass


# cmd = "python {0}/segment/predict.py --weights yolov5s-seg.pt --img 640 --conf 0.4 --source data/images".format(current_directory_path)
# cmd1 = "python {0}/yolov5/detect_custom.py --source {0}/input.png --weights {0}/yolov5/runs/train/exp/weights/best_tree.pt --img 640 --hide-conf --view-img --conf 0.25".format(current_directory_path)   



# while True:
# #     # replace this with your logic to receive the signal from the server
    
#     # result = ai_capture()
#     os.system(cmd1)
# #     print(result)

#     time.sleep(10)


    