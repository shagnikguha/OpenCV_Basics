import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
"""The new pixel intensity in the middle will be equal to the average of all surrounding pixel intensities"""
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
"""similar to avareagin, but each surrounding pixel is given a weight. More natural when compared to Averaging"""
gauss = cv.GaussianBlur(img, (3,3), 0)   # 0 = sigmaX = standard deviation in X direction
cv.imshow('Gaussian Blur', gauss)

# Median Blur
"""Noramally used to reduce noise. A low kernel size used"""
median = cv.medianBlur(img, 3) #instad of tuple, we use int for pararmeter 2(code assumes its a (3,3)tuple
cv.imshow('Median Blur', median)

# Bilateral
"""Applies blurring, but reatains edges"""
bilateral = cv.bilateralFilter(img, 10, 35, 25)#(image, diameter of pixel surroundings to take, SigmaColor: the number of colors to consider during blurring, SigmaSpace: how pixels away from the pixel will effect blurring )
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)


"""   
    Averaging Blurring is a simple and fast method that reduces noise but might blur edges.
    Gaussian Blurring is more advanced, preserving edges better due to the weighted averaging.
    Median Blurring is excellent for removing salt-and-pepper noise while maintaining edges.
    Bilateral Filtering is a more complex method that preserves edges and details, suitable for tasks
    where noise reduction is needed while retaining important features.
"""