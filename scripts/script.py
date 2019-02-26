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
	print("preparing to take picture...")
	with picamera.PiCamera() as camera:
		camera.resolution = (1280,720)
		stream = io.BytesIO()
		camera.capture(stream,'jpeg')
		connection.write(struct.pack('<L', stream.tell()))
		connection.flush()
		# Rewind the stream and send the image data over the wire
		stream.seek(0)
		connection.write(stream.read())
		print("sent to server")
		# Reset the stream for the next capture
		stream.seek(0)
		stream.truncate()
		print("===========================")


# clear files in images
dir_name = "./images"
[os.remove(os.path.join(dir_name,f)) for f in os.listdir(dir_name)]
try:
	# Connect a client socket to my_server:8000
	print("trying to connect to server")
	client_socket = socket.socket()
	client_socket.connect(('132.68.47.189', 8000))
	connection = client_socket.makefile('wb')
	print("connected to server succesfuly")
	#start the run
	print("==============================")
	for i in range(1,6):
		take_picture(i, connection)
		time.sleep(6)
finally:
	connection.close()
	client_socket.close()
