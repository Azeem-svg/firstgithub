import cv2 as cv
import numpy as np
from cv2 import resize
img = cv.imread('bct.jpg')
# print size
print("the size of our canvas is:", img.shape)

# resizefunction
resized_img = cv.resize(img, (450,450))

# gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#black & white img
(thresh, binary) = cv.threshold(resized_img, 127, 255, cv.THRESH_BINARY_INV)
kernal = np.ones((2, 2), np.uint8)
# _, thresh = cv2.threshold(img, 225, 255, cv2.THRESH_BINARY_INV)
# kernal = np.ones((2, 2), np.uint8)

#blurred img
# blurr_img = cv.GaussianBlur(resized_img, (13,13),0)

# adding circle
# cv.circle(resized_img,(250,200),80,(255,211,111))

# edge detection
# edge_img = cv.Canny(resized_img, 2,2)

# thikness of lines
# mat_kernel = np.ones((7,7), np.uint8)
# dialted_img = cv.dilate(edge_img, (mat_kernel), iterations=1)
dialted_img = cv.dilate(thresh, kernal, iterations=2)
contours, hierarchy = cv.findContours(dialted_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
objects = str(len(contours))
text = "Obj:"+str(objects)
cv.putText(dialted_img, text, (10, 25),  cv.FONT_HERSHEY_SIMPLEX,
            0.4, (240, 0, 159), 1)

#make thinner outline (erosion)
# ero_img= cv.erode(dialted_img, mat_kernel, iterations=1)



# cv.imshow("Original", img)
# cv.imshow("resized", resized_img)
cv.imshow("gra", resized_img)
cv.imshow("binary", binary)
# cv.imshow("blurrrr", blurr_img)
# cv.imshow("edges", edge_img)
cv.imshow("dialted", dialted_img)
# cv.imshow("erosion", ero_img)


cv.waitKey(0)

cv.destroyAllWindows()