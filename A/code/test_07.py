import xlrd
 
input_file_name = '../table/points_01.xls'
 

"""
从xls文件中读取数据
"""
workbook = xlrd.open_workbook(input_file_name)
print(workbook)
# 可以使用workbook对象的sheet_names()方法获取到excel文件中哪些表有数据
print(workbook.sheet_names())
# 可以通过sheet_by_index()方法或sheet_by_name()方法获取到一张表，返回一个对象
# table = workbook.sheet_by_index(0)
# print(table)
table = workbook.sheet_by_name('sheet1')
print(table)
# 通过nrows和ncols获取到表格中数据的行数和列数
rows = table.nrows
cols = table.ncols
# 可以通过row.values()按行获取数据，返回一个列表，也可以按列
#for row in range(rows):
#    row_data = table.row_values(row)
#    print(''.join(row_data))
# 也可以根据单元格获取每一个单元格的数据

points = [[314,688]]
x=[]
y=[]

for row in range(rows):
    if row<2:
        continue
    x.append(table.cell(row,0).value)
    y.append(table.cell(row,1).value)

    data = []
    for col in range(cols):
        data.append(table.cell(row, col).value)
    points.append(data)
    #print(data, end='\n')

#print(points,"\n")

#for i in range(len(points)):
    #print(points[i])

# print(x,"\n")
# print(y,"\n")

import numpy as np
from sklearn.cluster import KMeans

data = np.array(points) # 岩点数据，及以上问题的解法

岩点数量=115
阈值=10

# 聚类
kmeans = KMeans(n_clusters=岩点数量, random_state=0)
kmeans.fit(data)

# 获取聚类中心
centers = kmeans.cluster_centers_

# 合并相邻的聚类中心，获取每个岩点的代表点
represent_points = []
visited = np.zeros(岩点数量, dtype=bool)
for i, center in enumerate(centers):
    if visited[i]:  # 已经被标记为已访问
        continue
    # 查找相邻的聚类中心
    neighbors = []
    for j, candidate in enumerate(centers[i+1:]):
        if np.linalg.norm(center - candidate) < 阈值:
            neighbors.append(j+i+1)
    if not neighbors:  # 没有相邻的聚类中心
        represent_points.append(center)
        continue
    visited[i] = True
    # 将相邻的聚类中心和当前中心合并
    chosen_centers = np.insert(centers[neighbors], 0, center, axis=0)
    # 计算合并后的中心及其周围点的重心，作为代表点
    represent_point = np.mean(np.vstack([chosen_centers, data[kmeans.labels_ == i]]), axis=0)
    # 将当前聚类中心和相邻的聚类中心标记为已访问
    visited[neighbors] = True
    # 添加代表点
    represent_points.append(represent_point)

print(represent_points)



import xlwt

wb = xlwt.Workbook()

ws = wb.add_sheet('sheet1')

ws.write(0, 0, "x")
ws.write(0, 1, "y")
i = 1
for x,y in represent_points:
    ws.write(i,0,x)
    ws.write(i,1,y)
    i += 1
    
wb.save('../table/points_03.xls')