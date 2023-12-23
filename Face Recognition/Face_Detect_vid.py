import numpy as np
import cv2 as cv

vid = cv.VideoCapture(0)

while True:
    isTrue, frame = vid.read()
    feed = cv.flip(frame, 1)
    gray = cv.cvtColor(feed, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier("Face Recognition/haar_face.xml")
    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in face_rect:
        cv.rectangle(feed, (x,y), (x+w, y+h), (0,255,0), 2)
    cv.imshow("Webcam", feed)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
