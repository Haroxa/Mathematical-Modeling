import cv2
import numpy as np
src = cv2.imread("../image/read_02.jpg")
# cv2.namedWindow("input", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("input", src)
"""
提取图中的红色部分
"""
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
low_hsv = np.array([0,43,46])
high_hsv = np.array([10,255,255])
mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
# cv2.imshow("../image/test",mask)
cv2.imwrite("../image/color/red.jpg",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
low_hsv = np.array([11,43,46])
high_hsv = np.array([34,255,255])
mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
# cv2.imshow("../image/test",mask)
cv2.imwrite("../image/color/yellow.jpg",mask)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
low_hsv = np.array([35,43,46])
high_hsv = np.array([99,255,255])
mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
# cv2.imshow("../image/test",mask)
cv2.imwrite("../image/color/green.jpg",mask)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
low_hsv = np.array([100,43,46])
high_hsv = np.array([124,255,255])
mask = cv2.inRange(hsv,lowerb=low_hsv,upperb=high_hsv)
# cv2.imshow("../image/test",mask)
cv2.imwrite("../image/color/blue.jpg",mask)