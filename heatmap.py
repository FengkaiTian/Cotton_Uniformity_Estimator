import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

year1 = pd.read_csv("C:/Users/ft7b6/Desktop/Year1_cut/count_every_388.csv").iloc[:, 1:]
year2 = pd.read_csv("C:/Users/ft7b6/Desktop/Year2_cut/count_every_388.csv").iloc[:, 1:]

data = ~~~~ 


data_array = data.to_numpy()
colors = ["red", "yellow"]  
cmap = LinearSegmentedColormap.from_list("custom_red_yellow", colors, N=256)

plt.figure(figsize=(10, 6), dpi=600)  
heatmap = plt.imshow(data_array, aspect='auto', cmap=cmap, interpolation='none', vmin=0, vmax=45)
plt.colorbar(heatmap) 
plt.title('Year2')
plt.xlabel('Row')
plt.ylabel('Every_388cm')
plt.show()



















