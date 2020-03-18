import cv2 as cv
import datetime as dt

cap = cv.VideoCapture(0)

print((cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print((cap.get(cv.CAP_PROP_FRAME_HEIGHT)))

cap.set(3, 720)
cap.set(4, 720)

print(cap.get(3))
print((cap.get(4)))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        font = cv.FONT_HERSHEY_COMPLEX

        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(dt.datetime.now())

        frame = cv.putText(frame, datet, (10, 50), font, 1, (255, 0, 0), 2, cv.LINE_AA)
        frame = cv.circle(frame, (50,50), 10, (0,255,0), 5, cv.LINE_AA)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()
