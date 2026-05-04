import cv2
cap = cv2.VideoCapture("video.mp4")
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
for frame in reversed(frames):
    frame = cv2.resize(frame, (800, 500))
    cv2.imshow("Reverse", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
