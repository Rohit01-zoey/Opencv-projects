import cv2 as cv

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
print(cap.isOpened())
while cap.isOpened():
    ret, frame = cap.read()
    gr = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gr)
    print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    if cv.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release()
cv.destroyAllWindows()
