import cv2

image = cv2.imread('../resources/sample.jpg')

print(image.shape)
print(image.size)
print(image.dtype)
print(image[100,100])

roi = image[20:300, 20:300]

b,g,r = cv2.split(image)

blue = image[:,:,0]

cv2.imshow('Source', image)
cv2.imshow('ROI',roi)
cv2.imshow('Blue', blue)
cv2.imshow('Red', r)
cv2.waitKey()