# 导入模块，输出原图
import cv2
import matplotlib.pyplot as plt
bgr='../image/read_02.jpg'
rgb = cv2.imread(bgr)[:,:,::-1]
plt.imshow(rgb)
plt.show()
# 将图像转为HSV格式进而得到mask，HSV分别代表色相(Hue)、饱和度(Saturation)、明度(Value)
hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)

# 设定参数lowerb、upperb
import numpy as np
lowerb = np.array([100,100,100])
upperb = np.array([140,255,255])
# 获取mask
mask = cv2.inRange(hsv, lowerb, upperb)
# 利用mask进行颜色分离
masked = cv2.bitwise_and(bgr,bgr,mask=mask)

# 转回RGB格式
blue = cv2.cvtColor(masked,cv2.COLOR_BGR2RGB)
image_list = [rgb,hsv,mask,masked,blue]
title_list = ['rgb','hsv','mask','masked','blue']
plt.figure(figsize=(40,8))
for i in range(len(title_list)):
    plt.subplot(1,5,i+1)
    plt.imshow(image_list[i])
    plt.axis('off')
    plt.title(title_list[i],size=50)
plt.tight_layout()
plt.show()
