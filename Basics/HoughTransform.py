import cv2
import numpy as np
import matplotlib.pyplot as plt


def nothing(x):
    pass


img = cv2.imread('Data/Dog1.jpg', 0)
edges = cv2.Canny(img, 111, 212, apertureSize=3)
minLineLength = 20
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, minLineLength, maxLineGap)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread('Data/Dog1.jpg', 0)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=100)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
cv2.imshow('detected circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
