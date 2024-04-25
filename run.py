import cv2
import glob 
from predict_images_lib.predict_images import predict_image


list_img = glob.glob("C:/Users/ft7b6/Desktop/Year2_cut/png/*.png")

for i in list_img:
    loaded_image = cv2.imread(i)
    print(loaded_image)
    predict_image(loaded_image, file_name=i.split('.png')[0] + '.csv', 
                  model_path="C:/Users/ft7b6/runs/detect/train9/weights/best.pt")

















