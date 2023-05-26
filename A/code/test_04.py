# 各个颜色坐标点

import cv2
import numpy as np
import matplotlib.pyplot as plt
import xlwt

# 颜色处理，hsv查找 https://blog.csdn.net/qq_40456669/article/details/93375709
# 核心代码 https://blog.csdn.net/qq_45882682/article/details/123115247

# 需要先进入到 code目录下再运行，才不会报错
img = cv2.imread('../image/read_02.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

color_min = [ 0,26,35,100]
color_max = [10,34,77,124]
color_str = ["red","yellow","green","blue"]

for index in range (len(color_min)):
    print("i:",index," min: ",color_min[index]," max: ",color_max[index]," str: ",color_str[index])
    low_hsv = np.array([color_min[index], 43, 46])
    high_hsv = np.array([color_max[index], 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

    # 创建掩码的反向图像
    mask_inv = cv2.bitwise_not(mask)

    # 获取掩码区域和非掩码区域的像素
    # mask_pixels = cv2.bitwise_and(img, img, mask=mask)
    # inv_pixels = cv2.bitwise_and(img, img, mask=mask_inv)

    # 修复掩码区域的像素
    # output_img = cv2.inpaint(mask_pixels, mask, 3, cv2.INPAINT_TELEA)
    # output_img = cv2.inpaint(inv_pixels, mask, 3, cv2.INPAINT_TELEA)

    # 合并修复后的像素和未修复的像素
    # output_img = inv_pixels #cv2.add(output_img, inv_pixels)
    output_img = mask_inv
    # 显示修复后的图片
    cv2.imshow('Output Image', output_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(len(output_img))
    print(len(output_img[0]))

    list_y = []
    list_x = []

    for i in range(len(output_img)):
        # print(output_img[i])
        xmax = []
        for j in range(len(output_img[i])):
            if output_img[i][j] == 0:
                # print(output_img[i][j],j,i)
                list_x.append(j)
                list_y.append(len(output_img)-i)

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

    wb.save('../table/color/'+color_str[index]+'.xls')
