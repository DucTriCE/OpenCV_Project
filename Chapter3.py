import cv2
import numpy as np

img = cv2.imread("Data/lambo.jpg")
# print(img.shape) #Height, width, channel
imgResize = cv2.resize(img, (960, 640))
imgCropped = imgResize[:640, :300]

cv2.imshow("LamboResize", imgResize)
cv2.imshow("LamboCropped", imgCropped)

cv2.waitKey(0)