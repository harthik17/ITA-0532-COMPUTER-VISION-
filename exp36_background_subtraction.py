import cv2
cap = cv2.VideoCapture("video.mp4")
fgbg = cv2.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (800,500))
    fgmask = fgbg.apply(frame)
    cv2.imshow("Foreground Mask", fgmask)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
