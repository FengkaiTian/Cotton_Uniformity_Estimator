import pandas as pd
import numpy as np 

data = pd.read_csv("C:/Users/ft7b6/Desktop/Year1_cut/pixel_geo_row_weed_all_cotton.csv")
data['cumulative_center_y'] = np.nan 

max_value_of_row = max(data.no_row.unique())
min_value_of_row = min(data.no_row.unique())

for i in range(min_value_of_row, (max_value_of_row + 1)):
    print(i)
    current_img_row = data[data.no_row == i] 
    current_img_row_index = data[data.no_row == i].index
    culmulative_center_y =  data.loc[current_img_row_index, 'center_y'] + (data.loc[current_img_row_index, 'no_img_row'] - 1) * 1657
    data.loc[current_img_row_index, 'cumulative_center_y'] = culmulative_center_y
    

data.to_csv("C:/Users/ft7b6/Desktop/Year1_cut/culmulative_pixel_geo_row_weed_all_cotton.csv")











