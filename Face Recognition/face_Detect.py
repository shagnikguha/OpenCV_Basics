import numpy as np
import cv2 as cv

img = cv.imread("pics/lady.jpg")
cv.imshow("Face", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray) #harrcascade does not depend on color but on shapes

haar_cascade = cv.CascadeClassifier('Advanced/haar_face.xml') #cascade classifier will read the xml file at store it in a variable

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces found = {len(face_rect)}")

for (x, y, w, h) in face_rect:
    face = cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
cv.imshow("Marked", face)

cv.waitKey(0)