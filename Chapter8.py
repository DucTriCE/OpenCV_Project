import cv2
import numpy as np

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    countours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        # print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            param = cv2.arcLength(cnt, True)
            # print(param)
            approx = cv2.approxPolyDP(cnt, 0.02*param, True)
            ObjCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if ObjCor==3:
                ObjectType="TRI"
            elif ObjCor==4:
                aspRatio=w/float(h)
                if aspRatio>=0.95 and aspRatio<=1.05:
                    ObjectType="SQR"
                else:
                    ObjectType="REC"
            else:
                ObjectType="CIR"
            cv2.rectangle(imgContour, (x,y), (x+w,y+h), (0,255,0), 3)
            cv2.putText(imgContour, ObjectType, (x, y+10), cv2.FONT_ITALIC, 0.8, (100,155,255), 3)


path = 'Data/shapes.png'
img = cv2.imread(path)
imgContour = img.copy()
imgBlank = np.zeros_like(img)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
imgCanny = cv2.Canny(imgBlur, 50,50)
getContours(imgCanny)

imgStack = stackImages(0.6, ([img, imgGray, imgBlur],
                             [imgCanny, imgContour, imgBlank]))

# cv2.imshow("Original", img)
# cv2.imshow("imgGray", imgGray)
# cv2.imshow("imgBlur", imgBlur)
cv2.imshow("Stack Image", imgStack)
cv2.waitKey(0)