import cv2 as cv
import numpy as np

img = cv.imread('pics/city.jpeg')
cv.imshow('city', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None: #assuming we want to rotate around centre
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

R_rotated_rotated = rotate(rotated, -90)
cv.imshow('Rotated Rotated', R_rotated_rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #for shrinking use INTER_AREA
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)# 0 = flipping vertically(along x-axis), 1 = flipping horizontally(along y-axis), -1 is combo of both
cv.imshow('Flip', flip)

# Cropping
#cropped = img[50:50, 50:50]
#cv.imshow('Cropped', cropped)


cv.waitKey(0)