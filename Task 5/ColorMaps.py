'''
COLORMAP_AUTUMN = 0,
COLORMAP_BONE = 1,
COLORMAP_JET = 2,
COLORMAP_WINTER = 3,
COLORMAP_RAINBOW = 4,
COLORMAP_OCEAN = 5,
COLORMAP_SUMMER = 6,
COLORMAP_SPRING = 7,
COLORMAP_COOL = 8,
COLORMAP_HSV = 9,
COLORMAP_PINK = 10,
COLORMAP_HOT = 11
'''
import cv2

image = cv2.imread('../resources/sample.jpg')

rainbow = cv2.applyColorMap(image, cv2.COLORMAP_RAINBOW)

cv2.imshow('rainbow', rainbow)
cv2.waitKey()
cv2.destroyAllWindows()