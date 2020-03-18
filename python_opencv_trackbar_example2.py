import cv2 as cv
import numpy as np


def nothing(x):
    print(x)


cv.namedWindow('image')
cv.createTrackbar('CP', 'image', 10, 400, nothing)

switch = 'colorgray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while 1:
    img = cv.imread('/home/rohit/Downloads/lena.jpg')
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, str(pos), (50, 50), font, 3, (255, 0, 0), 3, cv.LINE_AA)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('/home/rohit/Downloads/lena.jpg', img)
cv.destroyAllWindows()
