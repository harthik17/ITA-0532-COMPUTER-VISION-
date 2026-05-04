import cv2
cap = cv2.VideoCapture("video.mp4")
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame,(800,500))
    cv2.imshow("Frame", frame)
    if cv2.waitKey(30) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
print("Use pytesseract for OCR")
