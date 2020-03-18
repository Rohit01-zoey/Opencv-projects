import cv2 as cv
import numpy as np

#img = cv.imread('/home/rohit/Downloads/lena.jpg', 1)

img = np.zeros([500,500,3], np.uint8)
img = cv.line(img, (0, 0), (255, 255), (255, 0, 0), 5, 8)
img = cv.arrowedLine(img, (255, 0), (500, 500), (255, 0, 0), 10)
img = cv.rectangle(img, (0, 0), (300, 600), (0, 255, 0), -1)
img = cv.circle(img, (300, 300), 20, (255, 0, 0), -1)
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, "opencv", (600, 600), font, 5, (0, 0, 255), 10, cv.LINE_AA)
cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
