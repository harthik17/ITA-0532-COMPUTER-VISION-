import cv2
eye = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
img = cv2.imread("image.jpg")
img = cv2.resize(img,(800,500))
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
eyes = eye.detectMultiScale(gray,1.3,5)
for (x,y,w,h) in eyes:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow("Eyes",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
