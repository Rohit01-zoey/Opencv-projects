import cv2 as cv

img = cv.imread("/home/rohit/Downloads/lena.jpg", 1)
print(img)
cv.imshow('image', img)
k = cv.waitKey(10000) & 0xFF
if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite('lena_copy.jpg', img)
    cv.destroyAllWindows()