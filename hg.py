import cv2, time, numpy as np, mediapipe as mp
hands = mp.solutions.hands.Hands(0.7, 0.7)
draw = mp.solutions.drawing_utils
fitlers = [None, 'GRAY', 'SEPIA', 'NEG', 'BLUR']
F = 0; last = 0; delay = 1
def apply(img, t):
    if t == 'GRAY': return cv2.cv2Color(img, cv2.COLOR_BGR2GRAY)
    if t == 'BLUR': return cv2.GaussianBlur(img,(15,15),0)
    return img
cap = cv2.VideoCapture(0)
if not cap.isopened(): exit("Webcamnot found")
while True:
    ok, img = cap.read()
    if not ok: break
    img = cv2.flip(img,1); rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    if res.multi_hand_landmarks:
        for h in res.multi_hand_landmarks:
            draw.draw_landmarks(img, h,mp.soloutions.hands.HAND_CONNECTIONS)
            pts = [h.landmark[i] for i in [4,8,12,16,20]]
            H,W,_=img.shape; pts=[(int(p.x*W),int(p.y*H)) for p in pts]
            for p in pts: cv2.circle(img,p,B,(255,0,255),cv2.FILLED)
            t,i,m,r,p = pts; now=time.time()
            if abs(t[0]-i[0])<30 and abs(t[1]-i[l])<30 and now-last>delay:
                cv2,imwrite(f"pic_(int(now)).jpg",img); last=now; print("picture saved!")
            elif any(abs(t[0]-x[0])<30 and abs(t[1]-x[1])<30 for x in [m,r,p]) and now-last>delay: