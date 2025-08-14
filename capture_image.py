#!/usr/bin/python
# capture_image.py
import cv2
import datetime
import glob
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def get_date_from_filename(filename):
    """Extracts the date from the filename and returns a datetime object."""
    # Example: Assuming date is in 'YYYY-MM-DD' format and is before the extension
    date_str = filename.split('/snapshot_')[-1].split('.')[0]
    return datetime.datetime.strptime(date_str, '%Y-%m-%d_%H:%M:%S')

cam = cv2.VideoCapture(0)

prime_num = 20
for x in range(prime_num):
    ret, frame = cam.read()
    if ret:
        print(f"Priming camera {x + 1}/{prime_num} times...")
    else:
        print("Failed to grab frame")
        x -= 1

ret, frame = cam.read()
if ret:
    filename = f"/home/lane/grow-tent-monitor/static/snapshots/snapshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}.jpg"
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

    image_filenames = glob.glob(f"/home/lane/grow-tent-monitor/static/snapshots/*.jpg")
    image_filenames = sorted(image_filenames, key=get_date_from_filename)

    frames = [Image.open(image) for image in image_filenames]
    start_frame = frames[0]
    end_frame = frames[-1]
    for x in range(10):
        frames.insert(0, start_frame)
    for x in range(10):
        frames.append(end_frame)
    frame_one = frames[0]
    frame_one.save("/home/lane/grow-tent-monitor/static/current_timelapse.gif", format="GIF", append_images=frames,
               save_all=True, duration=175, loop=0)
    print(f"Saved timelapse gif")
else:
    print("Failed to grab frame")
cam.release()
