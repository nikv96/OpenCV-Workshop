import cv2
import numpy as np

image = cv2.imread('../resources/sample.jpg', 0)
result = cv2.Canny(img, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Canny', result)