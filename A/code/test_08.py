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

#for i in range(len(points)):
#print(points)

'''
import math
centers = [[]]
ix = iy = i = 0
for x,y in points:
    if abs(ix-x)<=60 and abs(iy-y)<=35:
        continue
    ix=x ; iy=y
    centers.append([ix,iy])
    i+=1

print(centers)
print("len: ",i)

'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 读取数据
data = np.array(points)
# 聚类数量
k = 115
# 训练模型
model = KMeans(n_clusters=k)
model.fit(data)
# 分类中心点坐标
centers = model.cluster_centers_
print(centers)

import xlwt

wb = xlwt.Workbook()

ws = wb.add_sheet('sheet1')

ws.write(0, 0, "x")
ws.write(0, 1, "y")
i = 1
for x,y in centers:
    ws.write(i,0,x)
    ws.write(i,1,y)
    i += 1
    
wb.save('../table/points_02.xls')

'''
# 预测结果
result = model.predict(data)
print(result)

# 用不同的颜色绘制数据点
mark = ['or', 'og', 'ob', 'ok']
for i, d in enumerate(data):
    plt.plot(d[0], d[1], mark[result[i]%4])
# 画出各个分类的中心点
mark = ['*r', '*g', '*b', '*k']
for i, center in enumerate(centers):
    plt.plot(center[0], center[1], mark[i%4], markersize=20)

# 绘制簇的作用域
# 获取数据值所在的范围
x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1

# 生成网格矩阵
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
z = model.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)
cs = plt.contourf(xx, yy, z)
plt.show()
'''