import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('Data/Dog3.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# img = cv2.drawContours(img, contours, -1, (0, 255, 0), 0)
# plt.imshow(img, cmap='gray')
# plt.show()

# moments
cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt, True)

epsilon = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
img = cv2.drawContours(img, approx, -1, (0, 255, 0), 0)
plt.imshow(img, cmap='gray')
plt.show()

# bounding rectangle
x, y, w, h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)


(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0, 255, 0), 2)

# convexity defects
# ret, thresh = cv2.threshold(img, 127, 255, 0)
# contours, hierarchy = cv2.findContours(thresh, 2, 1)
# cnt = contours[0]
# hull = cv2.convexHull(cnt, returnPoints=False)
# defects = cv2.convexityDefects(cnt, hull)
# for i in range(defects.shape[0]):
#     s, e, f, d = defects[i, 0]
#     start = tuple(cnt[s][0])
#     end = tuple(cnt[e][0])
#     far = tuple(cnt[f][0])
#     cv2.line(img, start, end, [0, 255, 0], 2)
#     cv2.circle(img, far, 5, [0, 0, 255], -1)
#
# cv2.imshow('img', img)


# match shapes
# def match_shape(img1, img2):
#     ret, thresh = cv2.threshold(img1, 127, 255, 0)
#     ret, thresh2 = cv2.threshold(img2, 127, 255, 0)
#     contours, hierarchy = cv2.findContours(thresh, 2, 1)
#     cnt1 = contours[0]
#     contours, hierarchy = cv2.findContours(thresh2, 2, 1)
#     cnt2 = contours[0]
#     ret = cv2.matchShapes(cnt1, cnt2, 1, 0.0)
#     return ret


cv2.waitKey(0)
cv2.destroyAllWindows()
