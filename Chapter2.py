import cv2
import numpy as np

img = cv2.imread("Data/Tri.png")
kernel = np.ones((3,3), np.uint8)
img = cv2.resize(img, (540,680))

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Opencv image is BGR
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny =  cv2.Canny(img, 150, 50)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

# cv2.imshow("Gray image", imgGray)
# cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilation image", imgDilation)
cv2.imshow("Eroded image", imgEroded)

cv2.waitKey(0)