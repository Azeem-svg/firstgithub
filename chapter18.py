# how to change the prescriptives of a images
from turtle import width
import cv2 as cv
import numpy as np

img=cv.imread('down.jpg')
print(img.shape)

#defining points
point1=np.float32([[233,196],[82,471],[522,169],[715,482]])
width=152
height= 332
width, height=152,332
# point 2
point2=np.float32([[0,0],[332,0],[0,height],[width,height]])
#applying matrix
matrix=cv.getPerspectiveTransform(point1,point2)
out_img=cv.warpPerspective(img, matrix, (width, height))

cv.imshow('original', img)
cv.imshow('tranform', out_img)
# to save changed img
cv.imwrite('wer.png',out_img)
cv.waitKey(0)
cv.destroyAllWindows()

##homework