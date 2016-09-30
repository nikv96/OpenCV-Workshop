'''
Task 3 - Drawing Functions

line(imageObject, startPoint, endPoint, color, thickness) -> imageObject

rectangle(imageObject, startPoint, endPoint, color, thickness) -> imageObject

circle(imageObject, center, radius, color, thickness) -> imageObject

putText(imageObject, text, startPoint, font, scale, color, thickness, lineType)

ADDITIONAL TASK - Recreate the Olympics symbol as close as possible :)
'''

import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)

image = cv2.line(image, (0,0), (511, 511), (255,0,0), 5)

image = cv2.rectangle(image, (20,0), (100,100), (0, 255, 0), 5)

image = cv2.circle(image, (300,60), 50, (0,0,255), -1)

cv2.putText(image, 'iNTUition', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('Result', image)

cv2.waitKey()