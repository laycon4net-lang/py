import cv2, numpy as np
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: webcam not found"); exit()
lower_skin = np.array([0, 20, 70], np.uint8)
upper_skin = np.array([20, 255, 255], np.uint8)
while True:
    ret, frame = cap.read()
    if not ret: break
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
     cnt = max(contours, key=cv2.contourArea)
     if cv2.contourArea(cnt) > 500:
        x,y,w,h = cv2.boundingRect(cnt)
        cx, cy = x+w//2, y+h//2
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.circle(frame, (cx,cy), 5, (0,0,255), -1)
    cv2.imshow("Original", frame)
    cv2.imshow("Filterd", result)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()