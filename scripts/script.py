import os
import time
import picamera
import sys
sys.path.append("/home/pi/Desktop/scripts/detecting")
import detect


def calc_direction(image_path):
	return detect.find_balloon(image_path)


def move_drone():
	pass


def take_picture(image_num):
	print("preparing to take picture...")
	image_path = "images/image"+image_num+".jpg"
	with picamera.PiCamera() as camera:
		camera.resolution = (1280,720)
		camera.capture(image_path)
	print("calculating direction...")
	print(calc_direction(image_path))
	print("moving drone...")
	move_drone()
	print("==============================")


# clear files in images
dir_name = "./images"
[os.remove(os.path.join(dir_name,f)) for f in os.listdir(dir_name)]
#start the run
i = 1
print("==============================")
while 1:
	take_picture(str(i))
	i = i + 1
	# time.sleep(2)
