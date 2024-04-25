from ultralytics import RTDETR
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def predict_image(loaded_image,file_name,model_path):
    # check img type should be cv2 numpy array
    if not isinstance(loaded_image, np.ndarray):
        raise ValueError("img should be a numpy array")

    img_width = loaded_image.shape[1]
    img_height = loaded_image.shape[0]

    # slice to 2x2 images use cv2
    h, w, _ = loaded_image.shape
    top_left_image_segment = loaded_image[:h//2, :w//2]
    top_right_image_segment = loaded_image[:h//2, w//2:]
    bottom_left_image_segment = loaded_image[h//2:, :w//2]
    bottom_right_image_segment = loaded_image[h//2:, w//2:]

    # load model
    model = RTDETR(model_path)
    print(model.info())

    # predict 4 images
    results = model.predict(source=[top_left_image_segment, top_right_image_segment, bottom_left_image_segment, bottom_right_image_segment], conf=0.4)

    # show boxes info
    df_whole_boxes_info = pd.DataFrame(columns=['xmin', 'ymin', 'xmax', 'ymax', 'center_x', "center_y", 'confidence'])
    for i, _ in enumerate(results):
      print(len(results[i]))
      boxes = results[i].boxes.xyxy
      confidences = results[i].boxes.conf
      boxes = boxes.cpu().numpy()
      confidences = confidences.cpu().numpy()

      # image bias to original image, so that we can see the boxes in original image
      if i == 0: # top left image, no need to 
        pass
      elif i == 1: # top right image, bias x
        boxes[:, 0] += img_width // 2
        boxes[:, 2] += img_width // 2
      elif i == 2: # bottom left image, bias y
        boxes[:, 1] += img_height // 2
        boxes[:, 3] += img_height // 2
      elif i == 3: # bottom right image, bias x and y
        boxes[:, 0] += img_width // 2
        boxes[:, 2] += img_width // 2
        boxes[:, 1] += img_height // 2
        boxes[:, 3] += img_height // 2

      df_boxes_info = pd.DataFrame(boxes, columns=['xmin', 'ymin', 'xmax', 'ymax'])
      df_boxes_info['confidence'] = confidences
      df_boxes_info["center_x"] = (df_boxes_info['xmax'] + df_boxes_info['xmin']) / 2 
      df_boxes_info["center_y"] = (df_boxes_info['ymax'] + df_boxes_info['ymin']) / 2 
      df_whole_boxes_info = pd.concat([df_whole_boxes_info, df_boxes_info], ignore_index=True)

    # save to csv
    df_whole_boxes_info.to_csv(file_name, index=False)
    


