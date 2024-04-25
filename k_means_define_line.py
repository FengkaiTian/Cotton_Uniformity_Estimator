import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# 这个代码是假设是依据我之前的名字有no.pass
# 之后我分割了每个pass4行，每个pass单独做一次kmeans选出4行标注为1，2，3，4
# 以此类推，我有120行，那么我应该会有1~120行
# 该代码导出csv file expect有每颗棉花所在的no.row, no.pass, geo_x, geo_y, center_x, center_y, and so on. 

pd.set_option('display.precision', 20)
data = pd.read_csv("C:/Users/ft7b6/Desktop/Year1_cut/pixel_geo_all_cotton.csv", dtype={'geo_x': 'float64', 'geo_y': 'float64'})


############################## ignore first row and the last row
data = data[~data['no_row'].isin(["row1", "row81"])]
data.rename(columns={'no_row': 'no_img_row'}, inplace=True)
############################

for i in range(1, 31):
    print(i)
    filtered_data = data[data['no_pass'] == i]
    kmeans = KMeans(n_clusters=4)
    filtered_data['no_row'] = kmeans.fit_predict(filtered_data[['geo_x', 'geo_y', 'center_x']])
    filtered_data['no_row'] = filtered_data['no_row'] + 4 * (i-1)
    data.loc[data['no_pass'] == i, 'no_row'] = filtered_data['no_row']
    scatter = plt.scatter(filtered_data['geo_x'], filtered_data['geo_y'], c=filtered_data['no_row'])
    plt.show()

data.to_csv("C:/Users/ft7b6/Desktop/Year1_cut/pixel_geo_row_all_cotton.csv")


scatter = plt.scatter(data['geo_x'], data['geo_y'], c=data['no_row'])
plt.show()


