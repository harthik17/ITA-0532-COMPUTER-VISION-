import cv2
img = cv2.imread("image.jpg")
img = cv2.resize(img, (800, 500))
cv2.putText(img, "HELLO WOLF", (200,250),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.imshow("Text", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
