import cv2
import numpy as np

img = cv2.imread("image.jpg")

kernel = np.ones((5,5), np.uint8)
erode = cv2.erode(img, kernel, 1)

cv2.imshow("Original", img)
cv2.imshow("Erosion", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()