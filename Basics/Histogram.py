import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('Data/Dog1.jpg')
color = ('b', 'g', 'r')

for i, col in enumerate(color):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

# histogram equalization
# hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# cdf = hist.cumsum()
# cdf_normalized = cdf * hist.max() / cdf.max()
# plt.plot(cdf_normalized, color='b')
# plt.hist(img.flatten(), 256, [0, 256], color='r')
# plt.xlim([0, 256])
# plt.legend(('cdf', 'histogram'), loc='upper left')
# plt.show()
#
# cdf_m = np.ma.masked_equal(cdf, 0)
# cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# cdf = np.ma.filled(cdf_m, 0).astype('uint8')
# img2 = cdf[img]
#
# plt.imshow(img2, cmap='gray')
# plt.show()

img = cv2.imread('Data/Dog1.jpg', 0)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
plt.imshow(equ)
plt.title('Equalization')
plt.show()

# Adaptive Histogram Equalization
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
plt.imshow(cl1)
plt.title('Adaptive Equalization')
plt.show()

# 2D Histograms
img = cv2.imread('Data/Dog1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
plt.imshow(hist)
plt.title('2D Histograms')
plt.show()

