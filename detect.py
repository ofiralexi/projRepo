import tensorflow as tf
import sys
import os
import cv2
import numpy as np
import glob

# Import utilites
import label_map_util
import visualization_utils as vis_util

# Path to image
PATH_TO_IMAGE = '1.png'

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'

# Grab path to current working directory
CWD_PATH = os.getcwd()
# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH,MODEL_NAME,'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH,'training','labelmap.pbtxt')

# Number of classes the object detector can identify
NUM_CLASSES = 1

# Load the label map.
# Label maps map indices to category names, so that when our convolution
# network predicts `5`, we know that this corresponds to `king`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
	od_graph_def = tf.GraphDef()
	with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
		serialized_graph = fid.read()
		od_graph_def.ParseFromString(serialized_graph)
		tf.import_graph_def(od_graph_def, name='')

	sess = tf.Session(graph=detection_graph)

# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

MIN_CONFIDENCE = 0.85

def find_balloons(img_path):
    image = cv2.imread(img_path)
    image_expanded = np.expand_dims(image, axis=0)
    (boxes, scores, classes, num) = sess.run(
    	[detection_boxes, detection_scores, detection_classes, num_detections],
    	feed_dict={image_tensor: image_expanded})
    box = None
    vertical = ""
    horizontal = ""
    for i in range(scores.shape[1]):
        if scores[0,i]>MIN_CONFIDENCE:
            box = tuple(boxes[0][i].tolist())
            break
    if box:
        y_center = (box[0] + box[2])/2
        x_center = (box[1] + box[3])/2
        vertical = "up" if y_center < 0.45 else "down" if y_center > 0.55 else ""
        horizontal = "left" if x_center < 0.45 else "right" if x_center > 0.55 else ""
    return vertical + (" and " if vertical != "" and horizontal != "" else "") + horizontal


'''
# Load image using OpenCV and
# expand image dimensions to have shape: [1, None, None, 3]
# i.e. a single-column array, where each item in the column has the pixel RGB value
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)

# Perform the actual detection by running the model with the image as input
(boxes, scores, classes, num) = sess.run(
	[detection_boxes, detection_scores, detection_classes, num_detections],
	feed_dict={image_tensor: image_expanded})

print("boxes\n", boxes)
print("scores\n", scores)
print("classes\n", classes)
print("num\n", num)
print(image.shape)


count = 0
for i in range(scores.shape[1]):
    if scores[0,i]>0.8:
        print("    "+str(i+1)+".  "+str(category_index.get(classes[0,i])['name'])+"    ==>    "+str(scores[0,i]*100)+' %')
        print(boxes[0][i][0]*image.shape[0])
        print(boxes[0][i][1]*image.shape[1])
        print(boxes[0][i][2]*image.shape[0])
        print(boxes[0][i][3]*image.shape[1])
        count+=1

#540,960

print("\n	Total "+str(count)+" objects classified.\n")
vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=8,
    min_score_thresh=0.80)

cv2.imwrite("proccessed.jpg", image)
#cv2.imshow('Object detector', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
'''
