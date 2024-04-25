import pandas as pd 
import glob 



####################    find the geo file through csv name, and combine together, and export
pixel_file = glob.glob("C:/Users/ft7b6/Desktop/Year1_cut/pixel_positionCSV/*.csv")


for i in pixel_file:
    print(i)
    no_of_pass = i.split('\\')[1].split('_')[0]
    no_of_row = i.split('\\')[1].split('.csv')[0].split('_')[-1]
    geo_file = "C:/Users/ft7b6/Desktop/Year1_cut/geo_location/" + i.split('\\')[-1].split('.csv')[0] + "_geo.csv"
    pixel_df = pd.read_csv(i) 
    geo_df = pd.read_csv(geo_file)
    geo_df = geo_df.rename(columns={'x': 'geo_x', 'y': 'geo_y'})
    pixel_df["geo_x"] = geo_df["geo_x"]
    pixel_df["geo_y"] = geo_df["geo_y"]
    pixel_df["no_pass"] = no_of_pass
    pixel_df["no_row"] = no_of_row 
    print(no_of_pass)
    print(no_of_row)
    pixel_df.to_csv("C:/Users/ft7b6/Desktop/Year1_cut/combined_geo_pixel_location/" + i.split('\\')[-1])


######################################################################## combine所有geo  去visualize在QGIS
import pandas as pd 
import glob 
csv_files = glob.glob("C:/Users/ft7b6/Desktop/Year1_cut/combined_geo_pixel_location/*.csv")
combined_csv_files = pd.concat([pd.read_csv(f) for f in csv_files])
combined_csv_files.to_csv('C:/Users/ft7b6/Desktop/Year1_cut/pixel_geo_all_cotton.csv')





















































































