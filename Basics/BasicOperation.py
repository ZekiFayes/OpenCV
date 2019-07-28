"""
This is to go through the basic operations of opencv.
The goal is to familiarize myself with the operations.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


# image reading, show, writing
# '0 -> color'
# '1 -> gray'
# '-1 -> unchanged'

img = cv2.imread('Data/Dog1.jpg', 0)

# video Analysis
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# drawing functions
# line / circle / rectangle / ellipse / putText

img = cv2.circle(img, (100, 100), 20, (0, 0, 255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (100, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Trackbar

def nothing(x):
    pass


img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

switch = '0 : off\n1 : on'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()


# access pixel
# it is a three dimensional matrix
# 0 -> blue
# 1 -> red
# 2 -> green
img = cv2.imread('Data/Dog1.jpg')

# get shape
dim = img.shape

# total number of pixels
num_pixels = img.size

# dtype
num_type = img.dtype


# region of interest
'''
This is to select an area to manipulate.
It is very similar to select the region of a matrix
'''

# split and merge image channels
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# making borders for images (padding)
BLUE = [255, 0, 0]

replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(2, 3, 1), plt.imshow(img, 'gray'),  plt.title('ORIGINAL')
plt.subplot(2, 3, 2), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(2, 3, 3), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(2, 3, 4), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(2, 3, 5), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(2, 3, 6), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()

# arithmetic operations
# image blending

img1 = cv2.imread('Data/Dog1.jpg')
img2 = cv2.imread('Data/Dog3.jpg')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows, cols, channels = img2.shape
roi = img1[0: 100, 0: 100]
img = img2[0: 100, 0: 100]
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img, img, mask=mask)
dst = cv2.add(img1_bg, img2_fg)

img1[0: 100, 0: 100] = dst

cv2.imshow('res', img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
