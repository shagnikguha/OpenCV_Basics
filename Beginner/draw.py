import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8') #500 = height, 500 wight, 3 = color channels
cv.imshow('blanck',blank)
#img = cv.imread('pics/cat.jpeg')
#cv.imshow('cat',img)

''' 
#1. Paint the image a certain color
blank[200:300,200:300] = 0 , 0, 255   # type only : inside the square brackets to color entire image
cv.imshow('Green', blank)
'''

'''
# 2. Draw rectangle
cv.rectangle(blank, (0,0) , (250,250), (0,250,0), thickness = -1) #(0,0) and (250,250) define size of rectangle. (0,250,0) define color. Thickness can be any number to make an outline
cv.imshow('rectangle', blank)
'''

'''
#3. Draw circle
cv.circle(blank, (250,250), 10, (250,0,250), thickness = -1)
cv.imshow('cirlce', blank)
'''
'''
# 4. Draw line
cv.line(blank,(0,0), (50, 50), (0, 0, 250), thickness=3)
cv.imshow('line', blank)
'''
# 5. insert Text
cv.putText(blank, "__HELLO__", (250,250), cv.FONT_HERSHEY_DUPLEX, 1, (250,0,250), thickness=2)
cv.imshow('text', blank)
cv.waitKey(0)