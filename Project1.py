import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640) #Height
cap.set(4, 480) #Width
cap.set(10, 150) #Brightness

myColors = [[118,97,0,179,255,255],
            [22,84,0,115,255,217]]

myColorValue = [[0,0,255],
                [255,0,0]]

myPoints = []
def findColor(img, myColors, myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count=0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorValue[count], cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x, y, count])
        count+=1
        # cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
    countours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0,0,0,0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            param = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*param, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def draw(myPoints, myColorValue):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValue[point[2]], cv2.FILLED)

while True:
    _, img = cap.read()
    imgResult = img.copy()

    newPoints = findColor(img, myColors, myColorValue)
    if len(newPoints)!=0:
        for point in newPoints:
            myPoints.append(point)
    if len(myPoints)!=0:
        draw(myPoints, myColorValue)

    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break