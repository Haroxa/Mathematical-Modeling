import cv2
import numpy as np
import matplotlib.pyplot as plt
import xlwt

# 需要先进入到 code目录下再运行，才不会报错
img = cv2.imread('../image/read_02.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

color_min = [ 0,26,35,100]
color_max = [10,34,77,124]
color_str = ["red","yellow","green","blue"]

for i in range (len(color_min)):
    low_hsv = np.array([color_min[i], 0, 221])
    high_hsv = np.array([color_max[i], 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

    # print(len(mask))
    # print(len(mask[0]))

    list_y = []
    list_x = []

    for i in range(len(mask)):
        # print(mask[i])
        xmax = []
        for j in range(len(mask[i])):
            if mask[i][j] == 0:
                # print(mask[i][j],j,i)
                list_x.append(j)
                list_y.append(len(mask)-i)

    plt.plot(list_x, list_y, 'o', color='r')
    plt.show()

    wb = xlwt.Workbook()

    ws = wb.add_sheet('sheet1')

    ws.write(0, 0, "x")
    ws.write(0, 1, "y")
    i = 1
    for x in list_x:
        ws.write(i, 0, x)
        i += 1

    j = 1
    for y in list_y:
        ws.write(j, 1, y)
        j += 1

    wb.save('../table/color/'+color_str[i]+'.xls')
