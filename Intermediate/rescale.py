import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75): #works for images, pre-recorded and live videos
    width = int(frame.shape[1] * scale) #1 represents width
    height = int(frame.shape[0] * scale) #0 represents height
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('pics/cat.jpeg')
img_resized = rescaleFrame(img)
cv.imshow('cat', img)
cv.imshow('catR', img_resized)

capture = cv.VideoCapture('vids/testvid.mp4')

capture1 = cv.VideoCapture(0)

#outputting video
while True:
    isTrue, frame = capture.read()
    isTrue, frame1 = capture1.read()
    frame_resized = rescaleFrame(frame)
    frame_resized1 = rescaleFrame(frame1)
    cv.imshow('Video', frame)
    cv.imshow('VideoR', frame_resized)
    cv.imshow('Cam', frame1)
    cv.imshow('CamR', frame_resized1)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows