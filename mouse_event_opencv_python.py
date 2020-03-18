import cv2 as cv
import numpy as np


# events = [i for i in dir(cv) if 'EVENT' in i]
# print(events)
def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        #cv.circle(img, (x, y), 3, (0, 0, 255), -1)
        mycolorimage = np.zeros((512, 512, 3), np.uint8)
        mycolorimage[:] = [blue, green, red]

        cv.imshow('color', mycolorimage)


img = np.zeros((512, 512, 3), np.uint8)
#img = cv.imread('/home/rohit/Downloads/lena.jpg')
cv.imshow('image', img)
points = []
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()
