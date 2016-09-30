'''
Task 1 - Image Read, Display and Write.

HelloWorld application in opencv. It is a simple image read from your directory and display in a separate window.

#imread(filepath, [grayFlag])

grayFlag = 0 for grayscale

#imwrite(filepath, imageObject)
'''
import cv2

image = cv2.imread('../resources/sample.jpg', 0)

cv2.imshow('Result', image)

cv2.imwrite('../results/result.jpg', image)

cv2.waitKey()