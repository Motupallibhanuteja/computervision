import cv2
import numpy as np

image = cv2.imread('testimage.jpg')
kernel = np.ones((3,3), np.uint8)

image = cv2.dilate(image, kernel)
cv2.imshow('Dilated Image', image)
