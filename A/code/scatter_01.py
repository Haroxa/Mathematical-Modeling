# 读取坐标点数据
import xlrd
input_file_name = '../table/value/v_02.xls'
workbook = xlrd.open_workbook(input_file_name)
table = workbook.sheet_by_name('Sheet1')
rows = table.nrows
cols = table.ncols
points = []
for row in range(rows):
    if row<2:
        continue
    data = []
    for col in range(cols):
        data.append(table.cell(row, col).value)
    points.append(data)

import numpy as np
import matplotlib.pyplot as plt

# 构造数据
data = np.array(points)

# 定义颜色
colors = ['y', 'b', 'r', 'g']

# 绘制散点图并上色
for x,y,c in points:
    # print(x,y,c)
    plt.scatter(x, y , c=colors[int(abs(c)-1)])

# 设置图形属性
plt.box(True)
plt.axis([50,400,0,700])

# 显示图形
plt.show()