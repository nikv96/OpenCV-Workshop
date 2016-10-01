import cv2
import numpy as np

image = cv2.imread('../resources/sample.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('GrayScale', gray)
cv2.imshow('HSV', hsv)
cv2.waitKey()
cv2.destroyAllWindows()