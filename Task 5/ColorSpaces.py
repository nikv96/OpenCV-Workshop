'''
Task 5.1 - Color Spaces

cvtColor(ImageObject, ColorIndex)

This method allows you to change the color space of an image.
'''
import cv2

image = cv2.imread('../resources/lena.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('GrayScale', gray)
cv2.imshow('HSV', hsv)
cv2.waitKey()
cv2.destroyAllWindows()