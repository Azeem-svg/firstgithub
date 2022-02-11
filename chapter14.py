# how to draw lines and shapes in python
import cv2 as cv
import numpy as np

#draw a canvas 0 is for black 1 is for white
img = np.zeros((600,600))
img1 = np.ones((600,600))

#print size
print("the size of our canvas is:", img.shape)
# print(img)

## adding colors to canvas
colored_img = np.zeros((600,600,3),np.uint8) #channel addition

colored_img[:]= 255,0,255 # complete img color
# part img color
colored_img[150:230, 100:500]= 255,0,0

# adding line
cv.line(colored_img, (0,0),(300,300),(255,0,0),3)
# complete line
cv.line(colored_img, (0,0),(colored_img.shape[0],colored_img.shape[1]),(255,0,0),3)
# adding rectangle
cv.rectangle(colored_img,(50,100),(300,400),(255,240,0), 3)
#filling rectangle
cv.rectangle(colored_img,(50,100),(300,400),(255,240,0),cv.FILLED)
# adding circle
cv.circle(colored_img,(300,300),50,(255,100,0),cv.FILLED)

# adding text
cv.putText(colored_img,"azeem javed", (200,500), cv.FONT_HERSHEY_DUPLEX,1,(255,255,0),2)


# cv.imshow("cropped", img)
# cv.imshow("cro", img1)
cv.imshow("colred", colored_img)

cv.waitKey(0)

cv.destroyAllWindows()