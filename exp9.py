import cv2

img = cv2.imread("image.jpg")

big = cv2.resize(img, None, fx=2, fy=2)

cv2.imshow("Original", img)
cv2.imshow("Scaled Image", big)

cv2.waitKey(0)
cv2.destroyAllWindows()