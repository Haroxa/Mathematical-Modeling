import cv2
import numpy as np
import matplotlib.pyplot as plt
import xlwt

# 读取图片文件  // 需要先进入到 code目录下再运行，才不会报错
img = cv2.imread("../image/read_02.jpg")

# 转换为HSV颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义颜色范围，提取掩码
low_hsv = np.array([0, 0, 221])
high_hsv = np.array([180, 30, 255])
mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

# 获取非掩码区域的坐标
list_y = []
list_x = []
for i in range(len(mask)):
    for j in range(len(mask[i])):
        if mask[i][j] == 0:
            list_x.append(j)
            list_y.append(len(mask)-i)

# 生成新的图片
output_img = np.zeros_like(img)
for i in range(len(list_x)):
    x = list_x[i]
    y = list_y[i]
    output_img[y, x][0] = img[y, x, 0]
    output_img[y, x][1] = img[y, x, 1]
    output_img[y, x][2] = img[y, x, 2]

# 保存新的图片
cv2.imwrite('../image/output_01.jpg', output_img)