import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('Data/Dog1.jpg', 0)
# img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

# Erosion
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

# Dilation
dilation = cv2.dilate(img, kernel, iterations=1)

# opening
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# top hat
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# black hat
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


dst = [erosion, dilation, opening, closing, gradient, tophat, blackhat]
titles = ['erosion', 'dilation', 'opening', 'closing', 'gradient', 'tophat', 'balckhat']

i = 1
for item, t in zip(dst, titles):
    plt.subplot(2, 4, i), plt.imshow(item), plt.title(t)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
