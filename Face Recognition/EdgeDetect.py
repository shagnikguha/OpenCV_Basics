import numpy as np
import cv2 as cv
img = cv.imread("pics/city.jpeg")
cv.imshow("Img", img)

gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

#Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_t = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel x", sobel_x)
cv.imshow("Sobel y", sobel_y)
cv.imshow("Sobel combined", sobel_t)

#canny
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)
cv.waitKey(0)
