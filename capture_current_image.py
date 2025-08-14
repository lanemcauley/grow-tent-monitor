#!/usr/bin/python
# capture_image.py
import cv2
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

cam = cv2.VideoCapture(0)

for x in range(3):
    ret, frame = cam.read()
    if ret:
        print(f"Priming camera {x + 1}/3 times...")
    else:
        print("Failed to grab frame")
        x -= 1

ret, frame = cam.read()
if ret:
    filename = f"/home/lane/grow-tent-monitor/static/current_snapshot/current_snapshot.jpg"
    cv2.imwrite(filename, frame)

    img = Image.open(filename)
    draw = ImageDraw.Draw(img)

    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("/home/lane/grow-tent-monitor/sans-serif.ttf", 120)

    overlay_text = f"{datetime.datetime.now().strftime('%B %d, %Y - %H:%M:%S')}"

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((20, 20),overlay_text,(0,165,80),font=font, stroke_width=2, stroke_fill='black')

    img.save(filename)
    print("Saved", filename)
else:
    print("Failed to grab frame")
cam.release()