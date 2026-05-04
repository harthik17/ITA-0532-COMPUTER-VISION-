import numpy as np
import cv2
img = np.ones((500,500,3), dtype=np.uint8) * 255
cv2.rectangle(img,(0,0),(50,50),(0,0,0),-1)
cv2.rectangle(img,(450,0),(500,50),(255,0,0),-1)
cv2.rectangle(img,(0,450),(50,500),(0,255,0),-1)
cv2.rectangle(img,(450,450),(500,500),(0,0,255),-1)
cv2.imshow("Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
