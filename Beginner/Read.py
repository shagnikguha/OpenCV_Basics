import cv2 as cv

#img = cv.imread('pics/cat.jpeg')

#cv.namedWindow("cat", cv.WINDOW_NORMAL)

#cv.imshow('cat', img)

#capture = cv.VideoCapture('vids/testvid.mp4') #for a video
capture = cv.VideoCapture(2)   #0 for webcam   #6 wrking with c type connection

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows

#cv.waitKey(0)