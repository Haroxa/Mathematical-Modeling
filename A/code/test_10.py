import xlrd
 
input_file_name = '../table/points_01.xls'

workbook = xlrd.open_workbook(input_file_name)
print(workbook)

print(workbook.sheet_names())

table = workbook.sheet_by_name('sheet1')

rows = table.nrows
cols = table.ncols

points = [[314,688]]

for row in range(rows):
    if row<2:
        continue
    data = []
    for col in range(cols):
        data.append(table.cell(row, col).value)
    points.append(data)

from sklearn.cluster import AgglomerativeClustering
import numpy as np

# 岩点数据，两列分别为 x 和 y 坐标
rock_points = np.array(points)

# 进行最近邻聚类，不需要预设聚类数
model = AgglomerativeClustering(n_clusters=None, distance_threshold=130)
model.fit(rock_points)

# 输出聚类结果
labels = model.labels_
unique_labels = np.unique(labels)
clusters = []
for i in range(len(unique_labels)):
    current_cluster = rock_points[labels == unique_labels[i]]
    clusters.append(current_cluster)
    print(f"岩点簇{i+1}：{current_cluster[0]}")


import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1')
ws.write(0, 0, "x")
ws.write(0, 1, "y")

for i in range(len(unique_labels)):
    x=clusters[i][0][0] ; y=clusters[i][0][1]
    print("i: ",i , " x: ",x," y: ",y)
    ws.write(i+1,0,x)
    ws.write(i+1,1,y)

wb.save('../table/points_06.xls')