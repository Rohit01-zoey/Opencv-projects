import numpy as np
import cv2 as cv

img = cv.imread('/home/rohit/Downloads/lena.jpg', 1)
print(img.shape)
print(img.size)
print(img.dtype)
b, g, r = cv.split(img)
print(b)
img = cv.merge((b, g, r))

ball = img[1061:1121, 1550:1920]
img[1000:1060, 100:470] = ball
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
