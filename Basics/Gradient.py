import numpy as np
import matplotlib.pyplot as plt
import cv2


img = cv2.imread('Data/Dog3.jpg', 0)

# Sobel
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobelxy = sobelx + sobely

dst = [laplacian, sobelx, sobely, sobelxy]
titles = ['laplacian', 'sobelx', 'sobely', 'sobelxy']

i = 1
for item, t in zip(dst, titles):
    plt.subplot(2, 2, i), plt.imshow(item), plt.title(t)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
