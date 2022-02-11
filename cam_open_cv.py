# reading and displaying image
# import library
import cv2 as cv
import sys

from cv2 import cvtColor

# file visulaization
img=cv.imread('download.png')
cv.imshow("pehli image", img)

#resize img
# img= cv.resize(img,(800,600))

# conversion code
gray_img = cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("dosri image", img)

#file dispaly 
cv.waitKey(0)

