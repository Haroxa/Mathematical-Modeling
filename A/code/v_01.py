# 各个颜色坐标点

import cv2
import numpy as np
import matplotlib.pyplot as plt
import xlwt
from sklearn.cluster import AgglomerativeClustering


# 颜色处理，hsv查找 https://blog.csdn.net/qq_40456669/article/details/93375709
# 核心代码 https://blog.csdn.net/qq_45882682/article/details/123115247

# 需要先进入到 code目录下再运行，才不会报错
img = cv2.imread('../image/read_02.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

color_min = [ 0,26,35,100]
color_max = [10,34,77,124]
color_str = ["red","yellow","green","blue"]
value=[-3,-1,-4,-2]
threshold=[65,130,150,80]

wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1')
ws.write(0, 0, "x")
ws.write(0, 1, "y")
ws.write(0, 2,"value")

pos = int(1)

for index in range (len(color_min)):
    print("i:",index," min: ",color_min[index]," max: ",color_max[index]," str: ",color_str[index])
    low_hsv = np.array([color_min[index], 43, 46])
    high_hsv = np.array([color_max[index], 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

    # 创建掩码的反向图像
    mask_inv = cv2.bitwise_not(mask)
    output_img = mask_inv

    # list_y = []
    # list_x = []
    points =[]

    for i in range(len(output_img)):
        # print(output_img[i])
        xmax = []
        for j in range(len(output_img[i])):
            if output_img[i][j] == 0:
                points.append([j,len(output_img)-i])
                # print(output_img[i][j],j,i)
                # list_x.append(j)
                # list_y.append(len(output_img)-i)
    # print(points)
    rock_points = np.array(points)

    # 进行最近邻聚类，不需要预设聚类数
    model = AgglomerativeClustering(n_clusters=None, distance_threshold=threshold[index])
    model.fit(rock_points)

    print(color_str[index])
    # 输出聚类结果
    labels = model.labels_
    unique_labels = np.unique(labels)
    clusters = []
    for i in range(len(unique_labels)):
        current_cluster = rock_points[labels == unique_labels[i]]
        clusters.append(current_cluster)
        # print(f"岩点簇{i+1}: {current_cluster[0]}")
    print(len(unique_labels))
    for i in range(len(unique_labels)):
        x=clusters[i][0][0] ; y=clusters[i][0][1]
        x=int(x) ; y=int(y)             # 必须转换成内置的int型，否则写入时会报错
        print("i: ",i , " x: ",x," y: ",y)
        # print(np.isinf(x),np.isinf(y),np.isnan(x),np.isnan(y))
        ws.write(pos,0,x)
        ws.write(pos,1,y)
        ws.write(pos,2,value[index])
        pos += 1

wb.save('../table/value/v_01.xls')
