import cv2 as cv
from cv2 import aruco
import numpy as np

# Loading all pre-built libraries
ARUCO_DICT = {
	"DICT_4X4_50": cv.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv.aruco.DICT_APRILTAG_36h11
}

# Reading image
img = cv.imread('pics/map.png')

# Defining lists
corners = []
ID = []
centres = []
z_rot = []

# Checking the image with each prelaoded Libraries
for i in ARUCO_DICT.values():
    dictionary = aruco.getPredefinedDictionary(i)
    parameters = aruco.DetectorParameters()
    detector = aruco.ArucoDetector(dictionary, parameters)
    marker_corners, markers_ID, reject = detector.detectMarkers(img)
    #print(marker_corners, markers_ID)
    if marker_corners != () or markers_ID != None:
        corners.append(marker_corners)
        ID.append(markers_ID)
        break
    
    
# Calculating centre and angle of each marker
for mark in corners:
    for dv in mark:
        for c0,c1,c2,c3 in dv:
            mx = (c0[0]+c1[0]+c2[0]+c3[0])/4
            my = (c0[1]+c1[1]+c2[1]+c3[1])/4
            c = [mx,my]
            centres.append(c)
            vector = c0 - c
            angle = np.arctan2(vector[1], vector[0])
            angle *= 180/np.pi
            z_rot.append(abs(angle))
            

# Extracting corner points and creating a boundary
ID = ID[0].flatten().tolist()

boundary = [0, 0, 0, 0]

for i in range(len(ID)):
    if ID[i] == 5:  # top left
        boundary[0] = tuple(map(int, centres[i]))
    if ID[i] == 4:  # top right
        boundary[1] = tuple(map(int, centres[i]))
    if ID[i] == 6:  # bottom left
        boundary[2] = tuple(map(int, centres[i]))
    if ID[i] == 7:  # bottom right
        boundary[3] = tuple(map(int, centres[i]))

# Draw boundary lines
if all(boundary):
    cv.line(frame, boundary[0], boundary[1], (0, 255, 0), 2)
    cv.line(frame, boundary[1], boundary[3], (0, 255, 0), 2)
    cv.line(frame, boundary[3], boundary[2], (0, 255, 0), 2)
    cv.line(frame, boundary[2], boundary[0], (0, 255, 0), 2)


#print(boundary)

#corners = corners[0].flatten().tolist()  
# Calculating angle of each marker
# print(corners)
# print(ID)
# print(centres)
# print(z_rot)

# Updating image to show the values and data found
# aruco.drawDetectedMarkers(img, marker_corners, markers_ID, (0, 255, 0))

# for centre in centres:
#    cv.circle(img, (int(centre[0]), int(centre[1])), 5,(255,0,255), -1)

# cv.rectangle(img, tuple(map(int, boundary[0])), tuple(map(int, boundary[3])), (255, 0, 0), 5)

for i in range(len(boundary)-1):
    cv.line(img, boundary[i], boundary[i+1], (255,0,0), 5)
cv.line(img, boundary[i+1], boundary[0], (255,0,0), 5)


cv.imshow("img", img)

cv.waitKey(0)

