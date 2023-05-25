import cv2
import numpy as np

# 读取图片文件
img = cv2.imread("../image/read_02.jpg")

# 转换为HSV颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义颜色范围，提取掩码
low_hsv = np.array([0, 0, 221])
high_hsv = np.array([180, 30, 255])
mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

# 创建掩码的反向图像
mask_inv = cv2.bitwise_not(mask)

# 获取掩码区域和非掩码区域的像素
mask_pixels = cv2.bitwise_and(img, img, mask=mask)
inv_pixels = cv2.bitwise_and(img, img, mask=mask_inv)

# 修复掩码区域的像素
output_img = cv2.inpaint(mask_pixels, mask, 3, cv2.INPAINT_TELEA)

# 合并修复后的像素和未修复的像素
output_img = cv2.add(output_img, inv_pixels)

# 显示修复后的图片
cv2.imshow('Output Image', output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()