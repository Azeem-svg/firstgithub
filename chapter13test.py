import cv2 as cv
import numpy as np
img = cv.imread('download.png')
img = cv.resize(img,(500,700))
print("the size of our image is:", img.shape)
cropped_img = img(0:4, 0:3)

cv.imshow("original", img)
cv.imshow("cropped", cropped_img)

cv.waitKey(0)

cv.destroyAllWindows()