import os
import time
import picamera


def calc_direction():
	return "up"


def move_drone():
	pass


def take_picture(image_num):
	print("preparing to take picture...")
	with picamera.PiCamera() as camera:
		camera.resolution = (1280,720)
		camera.capture("images/image"+image_num+".jpg")
	print("calculating direction...")
	calc_direction()
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
	time.sleep(2)
