import os
from PIL import Image
import tifffile

tif_dir = "C:\\Users\\ft7b6\\Desktop\\Year1_cut"


for filename in os.listdir(tif_dir):
    if filename.endswith(".tif"):
        tif_path = os.path.join(tif_dir, filename)
        tif_image = tifffile.imread(tif_path)
        pil_image = Image.fromarray(tif_image)
        png_path = os.path.join(tif_dir, os.path.splitext(filename)[0] + ".png")
        pil_image.save(png_path)
        print(png_path)