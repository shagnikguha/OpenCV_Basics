import numpy as np
import cv2 as cv

apple = cv.VideoCapture("vids/appple.mp4")

while True:
    isTrue, frame = apple.read()
    
    # Converting to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    cv.GaussianBlur(hsv, (3,3), 0)

    # Color range
    lower_green = np.array([40, 40, 40])     # Lower HSV values for green
    upper_green = np.array([80, 255, 255])   # Upper HSV values for green
    mask_green = cv.inRange(hsv, lower_green, upper_green)

    
    """
    #USE TO SPECIFY THE REGION OF INTEREST 
    h, w, d = frame.shape
    search_top = 3*h/4
    search_bot = 3*h/4 + 20
    mask_green[0:int(search_top), 0:int(w)] = 0
    mask_green[int(search_bot):h, 0:int(w)] = 0
    """

    cv.imshow("Video", frame)
    cv.imshow("Mask", mask_green)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

