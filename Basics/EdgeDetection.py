import numpy as np
import matplotlib.pyplot as plt
import cv2


def nothing(x):
    pass


img = cv2.imread('Data/Dog1.jpg', 0)

cv2.namedWindow('image')
cv2.createTrackbar('T1', 'image', 0, 255, nothing)
cv2.createTrackbar('T2', 'image', 0, 255, nothing)


while 1:

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    T1 = cv2.getTrackbarPos('T1', 'image')
    T2 = cv2.getTrackbarPos('T2', 'image')

    edges = cv2.Canny(img, T1, T2)

    # cv2.imshow('image', img)
    cv2.imshow('image', edges)

cv2.destroyAllWindows()
