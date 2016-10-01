import cv2
import numpy as np

img = cv2.imread('../resources/sample.jpg')
image = cv2.imread('../resources/circle.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

circles = cv2.HoughCircles(gray_image,cv2.HOUGH_GRADIENT,1,70, param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(image,(i[0],i[1]),i[2],(0,255,0),2)

cv2.imshow('houghlines',img)
cv2.imshow('houghcircles',image)
cv2.waitKey()
cv2.destroyAllWindows()