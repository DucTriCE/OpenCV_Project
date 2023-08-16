import cv2
import numpy as np

img = cv2.imread("Data/Tri.png")

hor = np.hstack((img,img))
ver = np.vstack((img,img))


cv2.imshow("Horizontal", hor)
cv2.imshow("Vertical", ver)

cv2.waitKey(0)