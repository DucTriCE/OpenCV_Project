import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
# img[:] = (255, 0, 0)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0),3)
cv2.rectangle(img, (0,0), (250, 350), (0,0,255), cv2.FILLED)
cv2.circle(img, (450,50), 50, (255,0,0), 3)
cv2.putText(img, "OpenCV",(300,100), cv2.FONT_ITALIC,1,(255,255),5)
cv2.imshow("Image", img)
cv2.waitKey(0)