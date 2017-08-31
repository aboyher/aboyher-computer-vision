import cv2
import numpy as np

img = cv2.imread("images/image2.png")
red = img[:,:,2]
blue = img[:,:,0]

tup = [np.min(red), np.max(red), np.mean(red), np.std(red)]
print tup