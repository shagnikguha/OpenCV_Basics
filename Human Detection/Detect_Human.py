import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


while True:
    isTrue, frame = cam.read()
    output = frame

    Gframe = cv.cvtColor(frame.copy(), cv.COLOR_BGR2GRAY)
    Gframe = cv.GaussianBlur(Gframe, (5,5), 0)    

    boxes, weights = hog.detectMultiScale(Gframe, winStride=(8,8))

    #print(boxes)
    if len(boxes)>0:
        for (x, y, w, h) in boxes:
            output = cv.rectangle(output, (x,y), (x+w, y+h), (0,255,0), 2)
        
    cv.imshow("Gray", Gframe)
    cv.imshow("Marked", output)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows