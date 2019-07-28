import numpy as np
import matplotlib.pyplot as plt
import cv2

# Transformation
# Resize
img = cv2.imread('Data/Dog1.jpg')
# res = cv2.resize(img, (100, 100), interpolation=cv2.INTER_CUBIC)

# Translation
dim = img.shape

M1 = np.float32([[1, 0, 100], [0, 1, 50]])
dst1 = cv2.warpAffine(img, M1, (dim[1], dim[0]))

# Rotation
M2 = cv2.getRotationMatrix2D((dim[1]/2, dim[0]/2), 90, 1)
dst2 = cv2.warpAffine(img, M2, (dim[1], dim[0]))

# Affine Transform
pts1 = np.float32([[56, 65], [368, 52], [28, 387]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300]])

M3 = cv2.getAffineTransform(pts1, pts2)
dst3 = cv2.warpAffine(img, M3, (dim[1], dim[0]))

# Perspective Transform
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M4 = cv2.getPerspectiveTransform(pts1, pts2)
dst4 = cv2.warpPerspective(img, M4, (dim[1], dim[0]))


dst = [dst1, dst2, dst3, dst4]
titles = ['Translation', 'Rotation', 'Affine', 'Perspective']

i = 1
for item, t in zip(dst, titles):
    plt.subplot(2, 2, i), plt.imshow(item), plt.title(t)
    plt.xticks([]), plt.yticks([])
    i += 1
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
