from osgeo import gdal
import pandas as pd
import glob 

def pixel2coord(x, y):
    xoff, a, b, yoff, d, e = raster.GetGeoTransform()
    
    xp = a * x + b * y + a * 0.5 + b * 0.5 + xoff
    yp = d * x + e * y + d * 0.5 + e * 0.5 + yoff
    return(xp, yp)





list_tif = glob.glob("C:/Users/ft7b6/Desktop/Year2_cut/tif/*.tif")
list_csv = glob.glob("C:/Users/ft7b6/Desktop/Year2_cut/pixel_positionCSV/*.csv")
if len(list_tif) == len(list_csv):
    for j in range(0, len(list_tif)): 
        raster = gdal.Open(list_tif[j])
        data = pd.read_csv(list_csv[j])
        x = []
        y = []
        for i in range(0, len(data)):
            s = pixel2coord(data['center_x'][i], data['center_y'][i])
            xx= s[0]
            yy = s[1]
            x.append(xx)
            y.append(yy)
        geo_data = pd.DataFrame({'x': x, 'y': y})
        print(list_csv[i].split(".csv")[0] + "_geo.csv")
        geo_data.to_csv(list_csv[j].split(".csv")[0] + "_geo.csv")
else:
    ("Number of CSV and TIF not equal")



