'''
Task 6 - Canny Edge Detection

Canny(ImageObject, thresholds)

Canny Edge Detection.
'''
import cv2

image = cv2.imread('../resources/lena.jpeg', 0)
result = cv2.Canny(image, 100, 200)

cv2.imshow('Original', image)
cv2.imshow('Canny', result)

cv2.waitKey()