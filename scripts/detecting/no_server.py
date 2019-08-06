import io
from PIL import Image
import detect
import time

from fly_drone import *

arm_and_takeoff(50)
time.sleep(15)

for img_path in ['1.jpg','2.jpg','3.jpg']:
    vertical, horizontal = detect.find_balloons(img_path)
    direction = vertical + horizontal
    if direction == "" :
        direction = "forward"
        drive(direction)
        time.sleep(5)
    if vertical != "":
        drive(vertical)
        time.sleep(5)
    if horizontal != "":
        drive(horizontal)
        time.sleep(5)

    print(vertical, horizontal)

drive("r")
