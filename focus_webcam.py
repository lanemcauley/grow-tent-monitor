import cv2
import time

# Open the default camera (usually index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Wait for the camera to initialize
time.sleep(5) # Adjust the sleep time as needed

# Enable autofocus (set to 1)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

print("Webcam autofocus started!")
# Wait for a moment to allow autofocus to work
for x in range(10):
    for y in range(6):
        if(y > 0):
            if(x == 9):
                remaining_time = f"Autofocusing... {60 - (y * 10)} seconds remaining"
            else:
                remaining_time = f"Autofocusing... {9 - x} minutes {60 - (y * 10)} seconds remaining"
        else:
            remaining_time = f"Autofocusing... {10 - x} minutes remaining"
        print(remaining_time)
        time.sleep(10)


print("Autofocus complete!")

# Release the camera
cap.release()