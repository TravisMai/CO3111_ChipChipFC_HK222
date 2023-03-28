import torch
import os
from IPython.display import Image, clear_output, display # to display images
from roboflow import Roboflow
import glob
import shutil
import cv2

# def Webcam_720p():
#     cap.set(3,1280)
#     cap.set(4,720)

# cap = cv2.VideoCapture(0)
# Webcam_720p()

# while(True):
      
#     # Capture the video frame
#     # by frame
#     ret, frame = cap.read()
  
#     # Display the resulting frame
#     cv2.imshow('frame', frame)
      
#     # the 'q' button is set as the
#     # quitting button you may use any
#     # desired button of your choice
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
  
# # After the loop release the cap object
# cap.release()
# # Destroy all the windows
# cv2.destroyAllWindows()

# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp/weights/best.pt', force_reload=True) # image = Image.open("example.jpg")
# dataset_path = os.getcwd() + "/datasets"
# os.environ["DATASET_DIRECTORY"] = dataset_path

# # ------------------------------------------
# # please name a project in roboflow not upper caps
# proj_name = "Face-Detection"
# ver_num = "9"
# proj_folder = proj_name + "-" + ver_num
# path = f"/content/datasets/{proj_folder}/data.yaml"
# # ------------------------------------------

# rf = Roboflow(api_key="kZbzfRVKlT9GZeRpVHRv")
# project = rf.workspace("mohamed-traore-2ekkp").project("face-detection-mik1i")
# if not os.path.exists(dataset_path):
#     dataset = project.version(ver_num).download("yolov5")
# ------------------------------------------
current_directory_path = os.path.abspath(os.path.join(__file__, "..\..\content"))
print('__file__:    ', current_directory_path)
cmd = "python {0}\yolov5/detect.py --source img.jpg  --weights {0}\yolov5/runs/train/exp/weights/best.pt --img 640 --conf 0.25".format(current_directory_path)   
os.system(cmd)

# # rf = Roboflow(api_key="h4b0dmWWk0vEHM6Ocacd")
# # project = rf.workspace("bach-khoa-6k2sk").project(proj_name)
# # dataset = project.version(ver_num).download("yolov5")

# # os.system('python train.py --img 640 --batch 16 --epochs 200 --data {proj_path} --weights yolov5s.pt --cache')
# for i in range(5):
#     path_to_check = 'runs/detect/exp/'
#     if os.path.exists(path_to_check):
#         shutil.rmtree('runs/detect/exp/')
#     os.system("python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.1 --source ../datasets/{}/test/images".format(proj_folder))

