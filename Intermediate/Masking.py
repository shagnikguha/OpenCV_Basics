import cv2 as cv
import numpy as np

img = cv.imread('pics/monroe.jpg')
cv.imshow('M', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 ,img.shape[0]//2+45), 80, 255, -1)

rectangle = cv.rectangle(blank.copy(), (60,60), (270,270), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)