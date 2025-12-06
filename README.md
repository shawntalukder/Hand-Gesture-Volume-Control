# Hand Gesture-Based Volume Control Using Python, OpenCV & MediaPipe

This project implements a Real-time hand-gesture-controlled system for adjusting system volume (Volume Up / Volume Down) using a standard webcam.
The fingertip distance between the Thumb Tip and the Index Finger Tip is measured using MediaPipe Hands, and based on this distance, the system triggers keyboard volume actions using PyAutoGUI.

The project demonstrates how Computer Vision can be used to interact with the computer without any physical input devices. It is simple, fast, and completely real-time.


# 📌 Key Features

✔ Real-time hand detection using MediaPipe Hands

✔ Tracks thumb tip and index finger tip coordinates

✔ Calculates Euclidean distance

✔ Automatically triggers:

**Volume Up when distance ≥ 51**

**Volume Down when distance < 50**

✔ Uses a cooldown system to prevent repeated triggers

✔ Lightweight, no GPU required

✔ Works on Windows, Mac, and Linux

✔ Clean, modular, and easy to understand

# 📽 How It Works

The webcam captures each video frame.

1. MediaPipe detects hand landmarks (21 points).

2. The code extracts:

    **Thumb Tip → Landmark 4**

    **Index Tip → Landmark 8**

3. A line is drawn between them, and the distance is calculated.

4. If the distance is large → **Volume Up**
   If the distance is small → **Volume Down**
5. PyAutoGUI sends keyboard events to the system.

# 📦 Installation & Setup

Manually:

          pip install opencv-python mediapipe pyautogui numpy

# 🧠 Technologies Used
| Technology          | Purpose                          |
| ------------------- | -------------------------------- |
| **Python**          | Core programming language        |
| **OpenCV**          | Video capture, frame processing  |
| **MediaPipe Hands** | Hand landmark detection          |
| **PyAutoGUI**       | System keyboard control (volume) |
| **NumPy**           | Distance calculation             |

# ⚙️ Code Explanation (High-Level)

**Hand Detection**

MediaPipe returns coordinates of 21 hand landmarks.
We use only two:

| Landmark | Finger           | Index |
| -------- | ---------------- | ----- |
| 4        | Thumb Tip        | 4     |
| 8        | Index Finger Tip | 8     |


# Distance Calculation

Distance formula:

                distance = sqrt( (x2 - x1)^2 + (y2 - y1)^2 )
# Action Logic

      If distance ≥ 51 px → trigger Volume Up
      
      
      If distance < 50 px → trigger Volume Down
      
      
      A 0.5-second cooldown prevents repeated triggering.

# 📊 Demo Output (On Screen)

Green line + text → Volume Up

Red line + text → Volume Down

The line between thumb and index finger changes color to indicate active control.

# 🛡️ Cooldown System

To avoid fast spamming:
        if current_time - last_action_time > cooldown:
          pyautogui.press("volumeup")
          last_action_time = current_time
          
This keeps the system stable and prevents lag.

# 📌 Requirements

Python 3.7+

A working webcam

Windows / Linux / macOS


# 🤝 Contributing

Pull requests are welcome.

If you want to add features, fix bugs, or improve performance, feel free to contribute!


