import numpy as np
import cv2 as cv

img = cv.imread("pics/city.jpeg")
cv.imshow('Pic', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


#THRESHOLD
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #150 is set as the limit. If pixel intenstity is igher. pixel = white. else black
cv.imshow('THRESH', thresh)


#THRESHOLD INVERSE
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV) #150 is set as the limit. If pixel intenstity is igher. pixel = white. else black
cv.imshow('THRESH_INV', thresh_inv)

#Adaptive thresholding. Allowing computer to find the limit for thresholding.
adaptive_tresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Thresholding", adaptive_tresh)

cv.waitKey(0)