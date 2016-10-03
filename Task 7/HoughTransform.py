'''
Task 7 - Hough Transform

HoughLinesP()

Detect lines in an image.

HoughCircles()

Detect circles in an image.

Exercise - Find an image online with two circles. Detect the two circles with OpenCV and connect the centers with a line.
'''
import cv2
import numpy as np

img = cv2.imread('../resources/lines.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 50, 200, apertureSize = 3)

lines = cv2.HoughLines(edges, 1, np.pi/180, 10)

for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*a)
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

image = cv2.imread('../resources/circle.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray_image,cv2.HOUGH_GRADIENT,1,70, param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(image, (i[0], i[1]), i[2],(0, 255, 0), 2)

cv2.imshow('houghlines', img)
cv2.imshow('houghcircles', image)
cv2.waitKey()
cv2.destroyAllWindows()