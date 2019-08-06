print('yo')
import io
import socket
import struct
from PIL import Image
import detect


print('here')
# Start a socket listening for image_connections on 0.0.0.0:8000 (0.0.0.0 means
# all interfaces)
image_socket = socket.socket()
image_socket.bind(('0.0.0.0', 8000))
image_socket.listen(0)

direction_socket = socket.socket()
direction_socket.bind(('0.0.0.0', 8001))
direction_socket.listen(0)
print('listen')
# Accept a single image_connection and make a file-like object out of it
image_connection = image_socket.accept()[0].makefile('rb')
print('conenct')
direction_connection = direction_socket.accept()[0]
count = 1

#arm_and_takeoff(50)
#time.sleep(15)

dirs = ["right", "left", "up", "down"]

try:
	while True:
		# Read the length of the image as a 32-bit unsigned int. If the
		# length is zero, quit the loop
		image_len = struct.unpack('<L', image_connection.read(struct.calcsize('<L')))[0]
		if not image_len:
			print("NO MORE iM")
			continue
		# Construct a stream to hold the image data and read the image
		# data from the image_connection
		image_stream = io.BytesIO()
		image_stream.write(image_connection.read(image_len))
		# Rewind the stream, open it as an image with PIL and do some
		# processing on it
		image_stream.seek(0)
		image = Image.open(image_stream)
		print('Image is %dx%d' % image.size)
		#image.verify()
		print('Image is verified')

		img_path = 'out' + str(count) + '.jpg'
		count += 1
		image.save(img_path)
		print("HERE?")
		vertical, horizontal, y_center, x_center = detect.find_balloons(img_path)
		print (vertical)
		print (horizontal)
		print(y_center)
		print(x_center)
		direction = "forward"
		if x_center > 0:
			if vertical:
				direction += " " +vertical
			if horizontal:
				direction += " " + horizontal
		else:
			direction = "stay"
		direction_connection.send(direction.encode())
except Exception as e:
	print(e)
	print("DONE?")

finally:
	image_connection.close()
	image_socket.close()
	direction_connection.close()
	direction_socket.close()
