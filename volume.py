import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.6,
                       min_tracking_confidence=0.6)

cap = cv2.VideoCapture(0)

last_action_time = 0
cooldown = 0.5   # seconds delay to avoid repeated volume pressing

def get_distance(hand_landmarks, w, h):
    thumb_tip = 4
    index_tip = 8

    x1 = int(hand_landmarks.landmark[thumb_tip].x * w)
    y1 = int(hand_landmarks.landmark[thumb_tip].y * h)

    x2 = int(hand_landmarks.landmark[index_tip].x * w)
    y2 = int(hand_landmarks.landmark[index_tip].y * h)

    distance = np.hypot(x2 - x1, y2 - y1)
    return int(distance), (x1, y1), (x2, y2)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for lm in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

            distance, (x1, y1), (x2, y2) = get_distance(lm, w, h)

            current_time = time.time()

            # Draw distance line
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 3)

            # ---- VOLUME UP ----
            if distance >= 51:
                if current_time - last_action_time > cooldown:
                    pyautogui.press("volumeup")
                    last_action_time = current_time

                cv2.putText(frame, f"Distance: {distance} - Volume Up",
                            (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

            # ---- VOLUME DOWN ----
            elif 0 < distance < 50:
                if current_time - last_action_time > cooldown:
                    pyautogui.press("volumedown")
                    last_action_time = current_time

                cv2.putText(frame, f"Distance: {distance} - Volume Down",
                            (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 4)


    cv2.imshow("Volume Control", cv2.resize(frame, (800, 600)))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
