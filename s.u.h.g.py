import cv2
import time
import pyautogui
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Disable pyautogui failsafe
pyautogui.FAILSAFE = False

# Download model once from:
# https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task

MODEL_PATH = "hand_landmarker.task"

# MediaPipe Hand Landmarker
BaseOptions = python.BaseOptions
HandLandmarker = vision.HandLandmarker
HandLandmarkerOptions = vision.HandLandmarkerOptions
VisionRunningMode = vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1
)

landmarker = HandLandmarker.create_from_options(options)

# Webcam
cap = cv2.VideoCapture(0)
W, H = 640, 480
cap.set(3, W)
cap.set(4, H)

SCROLL = 300
DELAY = 1
last_time = time.time()

print("🖐 Gesture Scroll Active")
print("Open Palm → Scroll Up")
print("Fist → Scroll Down")
print("Press 'q' to quit")

def detect_gesture(landmarks):
    fingers = []

    # Index, Middle, Ring, Pinky
    for tip, pip in [(8,6),(12,10),(16,14),(20,18)]:
        fingers.append(landmarks[tip].y < landmarks[pip].y)

    # Thumb
    fingers.append(landmarks[4].x > landmarks[3].x)

    if sum(fingers) == 5:
        return "scroll_up"
    elif sum(fingers) == 0:
        return "scroll_down"
    else:
        return "none"

frame_id = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = landmarker.detect_for_video(mp_image, frame_id)
    frame_id += 1

    gesture = "none"

    if result.hand_landmarks:
        landmarks = result.hand_landmarks[0]
        gesture = detect_gesture(landmarks)

        for lm in landmarks:
            x, y = int(lm.x * W), int(lm.y * H)
            cv2.circle(frame, (x, y), 4, (0, 255, 0), -1)

        if time.time() - last_time > DELAY:
            if gesture == "scroll_up":
                pyautogui.scroll(SCROLL)
            elif gesture == "scroll_down":
                pyautogui.scroll(-SCROLL)
            last_time = time.time()

    cv2.putText(
        frame,
        f"Gesture: {gesture}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 0),
        2
    )

    cv2.imshow("🖐 Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
landmarker.close()
