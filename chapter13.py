# basic functions or manipulation in open cv
import cv2 as cv
import numpy as np
from cv2 import resize
img = cv.imread('azeem.jpeg')
# img = cv.resize(img, (50,70))
# resizefunction
resized_img = cv.resize(img, (450,250)) 

# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#black & white img
(thresh, binary) = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

#blurred img
blurr_img = cv.GaussianBlur(img, (7,7),0)
# edge detection
edge_img = cv.Canny(img, 47,47)
# thikness of lines
mat_kernel = np.ones((7,7), np.uint8)
dialted_img = cv.dilate(edge_img, (mat_kernel), iterations=-1)

#make thinner outline (erosion)
ero_img= cv.erode(dialted_img, mat_kernel, iterations=1)


# cropping with numpy
# print("the size of our image is:", img.shape)
# cropped_img = resized_img(0:200, 200:300)

cv.imshow("Original", img)
cv.imshow("resized", resized_img)
cv.imshow("gra", gray_img)
cv.imshow("blurrrr", blurr_img)
cv.imshow("edges", edge_img)
cv.imshow("dialted", dialted_img)
cv.imshow("erosion", ero_img)
cv.imshow("binary", binary)
cv.imshow("cropped", cropped_img)

cv.waitKey(0)

cv.destroyAllWindows()