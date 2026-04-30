import cv2

img = cv2.imread("image.jpg")

r = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original", img)
cv2.imshow("Rotate 270", r)

cv2.waitKey(0)
cv2.destroyAllWindows()