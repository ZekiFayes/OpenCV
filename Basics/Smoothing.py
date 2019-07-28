import numpy as np
import cv2
import matplotlib.pyplot as plt


# Convolution
img = cv2.imread('Data/Dog1.jpg')

kernel = np.ones((5, 5), np.float32) / 25
blur0 = cv2.filter2D(img, -1, kernel)

blur1 = cv2.GaussianBlur(img, (5, 5), 0)
blur2 = cv2.medianBlur(img, 5)
blur3 = cv2.bilateralFilter(img, 9, 75, 75)

blur = [blur0, blur1, blur2, blur3]
titles = ['Original', 'Gaussian', 'Median', 'Bilateral']

i = 1
for item, t in zip(blur, titles):
    plt.subplot(2, 2, i), plt.imshow(item), plt.title(t)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
