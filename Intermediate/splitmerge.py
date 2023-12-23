import cv2 as cv
import numpy as np

img = cv.imread('pics/city.jpeg')
cv.imshow('City', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

'''
This will show a gray image. Darker regions show higher concentration of that color
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)
'''

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)