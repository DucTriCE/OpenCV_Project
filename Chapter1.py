import cv2

#Import Image
# img = cv2.imread("Data/Tri.png")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

#Import video
# cap = cv2.VideoCapture("Data/road.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break

#Import webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640) #Height
cap.set(4, 480) #Width
cap.set(10, 100) #Brightness


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break