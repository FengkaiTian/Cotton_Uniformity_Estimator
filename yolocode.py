

import os
os.getcwd()
import sys
sys.path.insert(0, './yolov6.models')



!git clone https://github.com/WongKinYiu/yolov7


%cd yolov7
!pip install -r requirements.txt





rf = Roboflow(api_key="rPNLsxgFNgEPtqqmbest")
project = rf.workspace("fengkai-tian").project("mianhuayear2")
version = project.version(2)
dataset = version.download("yolov8")





from roboflow import Roboflow
rf = Roboflow(api_key="rPNLsxgFNgEPtqqmbest")
project = rf.workspace("fengkai-tian").project("mianhua2")
version = project.version(2)
dataset = version.download("yolov8")




from ultralytics import YOLO 
import torch 
import cv2
from PIL import Image
from ultralytics import RTDETR

model = YOLO('yolov8s.yaml')
model.info()
model = YOLO("C:/Users/ft7b6/yolov7/yolov8s.pt")






results = model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", epochs=10, imgsz=640, device=[0, 1], batch = 8, cos_lr = True, 
lr0 = 0.05, lrf = 0.05, verbose = False)





"""
model = YOLO('yolov8x.pt') 
results = model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", 
                      epochs=10600, imgsz=640, device=[0, 1], batch = 8, cos_lr = True, 
lr0 = 0.05, lrf = 0.05, verbose = False)



model = YOLO('yolov8x.pt') 
results = model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", 
                      epochs=10600, imgsz=640, device=[0, 1], batch = 4, cos_lr = True, 
lr0 = 0.1, lrf = 0.1, verbose = False)



model = YOLO('yolov8x.pt') 
results = model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", 
                      epochs=10600, imgsz=640, device=[0, 1], batch = 16, cos_lr = True, 
lr0 = 0.05, lrf = 0.05, verbose = False)
"""


model = RTDETR("rtdetr-x.pt") 






for i, (name, param) in enumerate(model.named_parameters()):
    print(i, name, param.requires_grad)
last_layer_name = [name for name, param in model.named_parameters() if param.requires_grad][range(-1, -30)]   
    
    
    
    
    
    
    

model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", 
            epochs=100, imgsz=640, device=[0, 1], batch = 32, cos_lr = True, 
lr0 = 0.001, lrf = 0.001, verbose = True)

model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", 
            epochs=50, imgsz=640, device=[0, 1], batch = 8, cos_lr = True, 
lr0 = 0.005, lrf = 0.005, verbose = True)


model.train(data = "C:/Users/ft7b6/yolov7/mianhua2-3/data.yaml", 
            epochs=50, imgsz=640, device=[0, 1], batch = 16, cos_lr = True, 
lr0 = 0.005, lrf = 0.005, verbose = True)



model.train(data = "C:/Users/ft7b6/yolov7/mianhuayear2full/data.yaml", 
            epochs=50, imgsz=640, device=[0, 1], batch = 32, cos_lr = True, 
lr0 = 0.005, lrf = 0.005, verbose = True, seed = 1)















############################################ Year2 

model = RTDETR("C:/Users/ft7b6/runs/detect/train/weights/best.pt")
model 


# Freeze
freeze = 30
freeze = [f'model.{x}.' for x in range(freeze)]  # layers to freeze
for k, v in model.named_parameters():
    v.requires_grad = True  # train all layers
    if any(x in k for x in freeze):
        print(f'freezing {k}')
        v.requires_grad = False


###############################################  unfreeze        

for param in model.parameters():
    param.requires_grad = True
####################################################

model.train(data = "C:/Users/ft7b6/mianhuaYear2-2/data.yaml",  epochs=150, imgsz=640, device=[0, 1], batch = 8, cos_lr = True, 
            lr0 = 0.005, lrf = 0.005)

metrics = model.val()


metrics = model.val(data = "C:/Users/ft7b6/mianhuaYear2-2/data.yaml") 
 











# 90 -> 139 
# 23 

import torch 
import cv2
from glob import glob 
import os 
import pandas as pd
import numpy as np 
import re
import torch.hub 


torch.cuda.is_available()

torch.cuda.get_device_name()

mod = torch.hub.load("C:/Users/ft7b6/yolov7", "custom", 
                     path_or_model = "C:/Users/ft7b6/yolov7/runs/train/exp34/weights/best.pt", source = "local", force_reload = True)

links = glob("C:/Users/ft7b6/yolov7/swdswdtry002/valid/images/*.jpg")
links = sorted(links)
links





data = []
result = []
freq = []
link = []
for i in links:
    b = mod(i)
    a = b.pandas().xyxy[0]
    a["links"] = i.split("\\")[-1].split('.')[0]
    result.append(a)

    
    
    
df = pd.DataFrame(data = {'xmin' : pd.Series(dtype='float'),
                          "ymin" : pd.Series(dtype='float'),
                          'xmax' : pd.Series(dtype='float'),
                          "ymax" : pd.Series(dtype='float')})

for i in range(0, len(result)):
    df = pd.concat((df, result[i]))
    
    
df.xmin = np.round(df['xmin']).astype(int)
df.ymin = np.round(df['ymin']).astype(int)
df.xmax = np.round(df['xmax']).astype(int)
df.ymax = np.round(df['ymax']).astype(int)
df



freq 
link
df


"C:/Users/ft7b6/yolov7/hubconf.py"





df.to_csv('C:/Users/ft7b6/yolov7/s.csv')


import cv2

df = df[df.confidence >= 0.3].reset_index()
for i in range(0 ,len(df)):
  da = cv2.rectangle(data[0], (df.xmin[i], df.ymin[i]), (df.xmax[i], df.ymax[i]), (255, 0, 0), 2)


cv2.imshow("img", da)
  
cv2.waitKey(0)
cv2.destroyAllWindows()









df = pd.DataFrame(data = {'xmin' : pd.Series(dtype='float'),
                          "ymin" : pd.Series(dtype='float'),
                          'xmax' : pd.Series(dtype='float'),
                          "ymax" : pd.Series(dtype='float'),
                          })

for i in range(0, len(result)):
  df = pd.concat((df, result[i]))
df.xmin = np.round(df['xmin']).astype(int)
df.ymin = np.round(df['ymin']).astype(int)
df.xmax = np.round(df['xmax']).astype(int)
df.ymax = np.round(df['ymax']).astype(int)




























rf = Roboflow(api_key="RMUIfNtoaZUK6JSxEZhr")
project = rf.workspace("datasets-ipeox").project("swdswdtry001")
dataset = project.version(11).download("yolov7")





!python train.py --batch 4 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7_training.pt
!python train.py --batch 6 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7_training.pt
!python train.py --batch 8 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7_training.pt
!python train.py --batch 10 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7_training.pt
    


!python train.py --batch 4 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7x_training.pt
!python train.py --batch 6 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7x_training.pt
!python train.py --batch 8 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7x_training.pt
!python train.py --batch 10 --epochs 400 --data C:/Users/ft7b6/yolov7/swdswdtry001/data.yaml --weights C:/Users/ft7b6/yolov7/yolov7x_training.pt












mianhua year 1 
grid 3.85
rotate -1.45





























