import os
import time
import sys
import io
import socket
import struct


def calc_direction():
	pass


def move_drone():
	pass


def take_picture(imagenum, connection):
	pass

try:
	# Connect a client socket to my_server:8000 for sending images
	print("trying to connect socket 1")
	client_images = socket.socket()
	client_images.connect(('10.0.0.59', 8000))
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
