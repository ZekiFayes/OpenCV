import numpy as np
import cv2
import matplotlib.pyplot as plt


def nothing(x):
    pass


img = cv2.imread('Data/coin.png', 0)
ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations=3)
# Finding sure foreground area
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret1, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
# # Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
# # Marker labelling
ret2, markers = cv2.connectedComponents(sure_fg)
# # Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# # Now, mark the region of unknown with zero
markers[unknown == 255] = 0
# markers = markers.astype('int32')

img1 = cv2.imread('Data/coin.png', 1)
markers = cv2.watershed(img1, markers)
img1[markers == -1] = [255, 0, 0]

image = [img, opening, sure_bg, dist_transform, sure_fg, unknown, markers, img1]
name = ['img', 'opening', 'sure_bg', 'dist_transform', 'sure_fg', 'unknown', 'markers', 'img1']

i = 1
for n, img in zip(name, image):
    plt.subplot(2, 4, i), plt.imshow(img), plt.title(n)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
