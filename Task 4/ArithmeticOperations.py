'''
Task 4.2 - Arithmetic Operations


#addWeighted(Image1Object, weight, Image2Object, weight, GammaFactor)

Add Weighted allows you to blend two images giving certain weightage to each image.
'''
import cv2
import numpy as np

image1 = cv2.imread('../resources/lena.jpeg')
image2 = cv2.imread('../resources/logo.png')

image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

waterMark = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

cv2.imshow('result', waterMark)
cv2.waitKey()
cv2.destroyAllWindows()