import glob
import os 

##########################################以下代码是给图片附上每一个row的标签如：将“year1_300”变成“1_year1_300”

tif_file_paths = []
for i in range(0, 2431):
    tif_file_paths.append("C:/Users/ft7b6/Desktop/Year1_cut/year1_" + str(i) + ".tif")

for index, file_path in enumerate(tif_file_paths):
    group_number = ((index) // 81) + 1  # 计算组号
    new_file_path = file_path.replace("year1", f"{group_number}_year1")
    os.rename(file_path, new_file_path)  

##########################################以下代码是给图片附上每一个row的标签如：将“1_year1_300"变成“1_year1_(第几行)"

num_groups = 2430 / 81 
print(int(num_groups))

link = glob.glob('C:/Users/ft7b6/Desktop/Year1_cut/*.tif')
for i in link:
    group_number = (int(i.split("_")[-1].split('.')[0])) % 81 + 1  # 计算组号
    new_file_link = i.rsplit("_", 1)[0] + "_row" + str(group_number) + ".tif"
    print(new_file_link)
    os.rename(i, str(new_file_link))  
