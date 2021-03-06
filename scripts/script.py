import os
import time
import sys
import io
import socket
import struct
from fly_drone import *
import picamera

camera = picamera.PiCamera()
camera.resolution = (2592,1944)
time.sleep(30)


def take_picture(imagenum, connection):
	if imagenum == 5: #send signal we're done
		connection.write(struct.pack('<L', 0))
		return
	stream = io.BytesIO()
	camera.capture(stream,'jpeg')


	time.sleep(1)
	connection.write(struct.pack('<L', stream.tell()))
	connection.flush()
	# Rewind the stream and send the image data over the wire
	stream.seek(0)
	connection.write(stream.read())


	with open("tmp" + str(imagenum) + ".jpg","wb+") as f:
		stream.seek(0)
		f.write(stream.read()) 
	print("picture "+str(imagenum)+" sent to server")
	# Reset the stream for the next capture
	stream.seek(0)
	stream.truncate()
	direction = client_directions.recv(1024).decode()
	print("=== direction:" + direction)
	print(direction.split(" "))
	for dir in direction.split(" "):
		drive(dir)
		time.sleep(1)
	# time.sleep(1)
	print("----------")


try:
	ip = "192.168.137.1"
	# Connect a client socket to my_server:8000 for sending images
	print("trying to connect socket 1")
	client_images = socket.socket()
	client_images.connect((ip , 8000))
	connection = client_images.makefile('wb')
	# Connect a client socket to my_server:8001 for recieving inputs
	print("trying to connect socket 2")
	client_directions = socket.socket()
	client_directions.connect((ip , 8001))
	print("connected to server succesfuly")
	#start the run
	print("========== taking off ==========")
	arm_and_takeoff(2)
	# time.sleep(3)
	print("==============================")
	for i in range(1,20):
		take_picture(i, connection)

finally:
	print("rtl")
	drive('r')
	connection.close()
	client_images.close()
	client_directions.close()
