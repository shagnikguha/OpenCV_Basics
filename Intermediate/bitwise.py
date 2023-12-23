import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), (255,255,255), -1)
circle = cv.circle(blank.copy(), (200,200), 200, (255,255,255), -1)
"""Only using blanck inside the paramteters will change the actual blanck image as well. Use .copy after blanck to make sure blanck img is not altered"""

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

#Bitwise AND  (Only regions common to both images is returned)
bit_AND = cv.bitwise_and(rectangle,circle)
cv.imshow("AND", bit_AND)

#bitwise OR  (returns a combination of both images)
bit_OR = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bit_OR)

#bitwise XOR (returns the part of the images that are not common)
bit_XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bit_XOR)

#bitwise NOT (return the opposite of an image. i.e. the unnocupied regions become occupied and vice versa)
bit_NOT = cv.bitwise_not(rectangle)
cv.imshow("NOT", bit_NOT)

cv.waitKey(0)