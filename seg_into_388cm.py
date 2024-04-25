import pandas as pd
import numpy as np


data = pd.read_csv("C:/Users/ft7b6/Desktop/Year1_cut/culmulative_pixel_geo_row_weed_all_cotton.csv")

# 2022
# 1657 * 79 = 130903 
# grid = 3.85m
# GSD = 2.3mm / pixel 


# 2023 
# 1412 * 79 = 111548
# grid = 3.85m
# GSD = 2.7mm / pixel 


max_value = 130903                    # change
interval = 1657                       # change
num_intervals = max_value // interval
count_df = pd.DataFrame(np.zeros((79, 120)), columns=[f'no_row_{i}' for i in range(120)])
count_df.index = range(1, 80)

for i in range(120):
    counts = data.loc[data['no_row'] == i, 'no_img_row'].value_counts().sort_index(ascending=True)
    count_df.loc[counts.index, f'no_row_{i}'] = counts.values
    
    

    
count_df.to_csv("C:/Users/ft7b6/Desktop/Year1_cut/count_every_388.csv")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    