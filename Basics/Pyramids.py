import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Data/Dog1.jpg', 1)

G = img.copy()
gp = [G]

for i in range(6):
    G = cv2.pyrDown(G)
    gp.append(G)

plt.figure(1)
i = 1
for item in gp:
    plt.subplot(2, 4, i), plt.imshow(item), plt.title('fig' + str(i))
    plt.xticks([]), plt.yticks([])
    i += 1

lgp = [gp[5]]
for i in range(5, 0, -1):
    GE = cv2.pyrUp(gp[i])
    lgp.append(GE)

plt.figure(2)
i = 1
for item in lgp:
    plt.subplot(2, 4, i), plt.imshow(item), plt.title('fig' + str(i))
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()


