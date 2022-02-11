# convert an image into black and white saving converted poic
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite

# reading image
img = cv.imread('aze.jpg')
# converting into gray
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#  converting into binary
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# Saving img
imwrite('image_gray.png', gray)
imwrite('image_gr.png', binary)
# displaying img
cv.waitKey(0)
# destroying all windows
cv.destroyAllWindows()
