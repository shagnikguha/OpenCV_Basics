import cv2 as cv
import numpy as np

camera = cv.VideoCapture('vids/balT.mp4')

while True:
    isTrue, frame = camera.read()
    output = frame

    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    #mask_green = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    lower_green = np.array([40, 50, 50])    
    upper_green = np.array([85, 255, 255])   
    mask_green = cv.inRange(hsv_frame, lower_green, upper_green)

    #grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(mask_green, (3,3), 0)    
    
    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, dp=1, minDist=20, param1=55, param2=16, minRadius=20, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(output,(i[0],i[1]),2,(0,0,255),3)
        
    #cv.imshow('masked', mask_green)
    
    cv.imshow('gray', blurFrame)
    
    cv.imshow('cam', output)
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

camera.release()
cv.destroyAllWindows