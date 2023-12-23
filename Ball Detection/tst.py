import cv2 as cv
import numpy as np

vid = cv.VideoCapture('vids/appple.mp4')

while True:
    isTrue, frame = vid.read()

    cv.imshow("vid", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows