"""
This is to try to understand features: Corners, edges, etc.
This is to describe the figure.
Along with Segmentation, we can further take a close look at the object.
If we use classification methods, then we can recognize the object.
This is object recognition.
Now that we have learnt deep learning. Here we are focused segmentation and feature detection
such that we can build a system by using these libraries. Each library will be implemented the
specific functionalities, which reduces the dependencies.
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt


# Harris
def nothing(x):
    pass


img = cv2.imread('Data/Dog1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

cv2.namedWindow('image')
cv2.createTrackbar('Neighbor_k', 'image', 2, 20, nothing)
cv2.createTrackbar('Sobel_k', 'image', 2, 20, nothing)
cv2.createTrackbar('Equation_k', 'image', 1, 100, nothing)
cv2.createTrackbar('Threshold_k', 'image', 1, 100, nothing)

while 1:

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    T1 = cv2.getTrackbarPos('Neighbor_k', 'image')
    T2 = cv2.getTrackbarPos('Sobel_k', 'image')
    T3 = cv2.getTrackbarPos('Equation_k', 'image')
    T4 = cv2.getTrackbarPos('Threshold_k', 'image')

    if T2 % 2 == 0:
        T2 += 1

    dst = cv2.cornerHarris(gray, T1, T2, T3/100)
    dst = cv2.dilate(dst, None)
    img[dst > T4/100 * dst.max()] = [0, 0, 255]

    cv2.imshow('dst', img)

cv2.destroyAllWindows()


# Shi-Tomasi
img = cv2.imread('Data/Dog1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, 3)

plt.imshow(img, cmap='gray')
plt.show()


# SIFT
img = cv2.imread('Data/Dog1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sift = cv2.()


# SURF
surf = cv2.SURF()



