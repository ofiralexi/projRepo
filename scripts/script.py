import os
import time
import picamera
import sys
import io
import socket
import struct


def calc_direction():
	pass


def move_drone():
	pass


def take_picture(imagenum, connection):
	if imagenum == 5: #send signal we're done
		connection.write(struct.pack('<L', 0))
		return
	with picamera.PiCamera() as camera:
		camera.resolution = (1280,720)
		stream = io.BytesIO()
		camera.capture(stream,'jpeg')
		connection.write(struct.pack('<L', stream.tell()))
		connection.flush()
		# Rewind the stream and send the image data over the wire
		stream.seek(0)
		connection.write(stream.read())
		print("picture "+str(imagenum)+" sent to server")
		# Reset the stream for the next capture
		stream.seek(0)
		stream.truncate()
		print("=== direction:" + client_directions.recv(1024).decode())
		print("----------")


try:
	# Connect a client socket to my_server:8000 for sending images
	print("trying to connect socket 1")
	client_images = socket.socket()
	client_images.connect(('132.68.47.189', 8000))
	connection = client_images.makefile('wb')
	# Connect a client socket to my_server:8001 for recieving inputs
	print("trying to connect socket 2")
	client_directions = socket.socket()
	client_directions.connect(('132.68.47.189', 8001))
	print("connected to server succesfuly")
	#start the run
	print("==============================")
	for i in range(1,6):
		take_picture(i, connection)
		time.sleep(2)
finally:
	connection.close()
	client_images.close()
	client_directions.close()
