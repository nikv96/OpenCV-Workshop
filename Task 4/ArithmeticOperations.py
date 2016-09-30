import cv2
import numpy as np

image1 = cv2.imread('sample.jpg')
image2 = cv2.imread('logo.jpg')

waterMark = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

cv2.imshow('result', waterMark)
cv2.waitKey()
cv2.destroyAllWindows()