import numpy as np
import cv2
img = np.ones((500,500,3), dtype=np.uint8) * 255
cv2.circle(img,(250,250),100,(0,255,0),3)
cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
