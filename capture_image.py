# capture_image.py
import cv2
import datetime

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
if ret:
    filename = f"static/snapshots/snapshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
    cv2.imwrite(filename, frame)
    print("Saved", filename)
else:
    print("Failed to grab frame")
cam.release()