#!/usr/bin/python
# capture_image.py
import cv2
import datetime

cam = cv2.VideoCapture(0)
ret, frame = cam.read()
if ret:
    filename = f"/home/lane/grow-tent-monitor/static/current_snapshot/current_snapshot.jpg"
    cv2.imwrite(filename, frame)
    print("Saved", filename)
else:
    print("Failed to grab frame")
cam.release()