# joining two images


import cv2 as cv

import numpy as np
img = cv.imread("download.png")

# stacking img
# horizontle stack

hor_img=np.hstack((img,img))
# verticle stack
ver_img= np.vstack((img,img))

# cv.imshow('horizontle', hor_img)
cv.imshow('verticle', ver_img)
cv.waitKey(0)
cv.destroyAllWindows()
# you can stack images with same shape(width, height, color, channel)
# you have to define a function to stack multiple images of different sizes and shapes
#we cannot resixe a stack img(but with a function)
#same number of channels to use np functions