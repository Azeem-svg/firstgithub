#coordinates of an image or video
#bgr color codes for image
import cv2 as cv
import numpy as np
#step 2 define a function
def find_coord(event, x, y, flags, params):
    if event== cv.EVENT_LBUTTONDOWN:
     
       #left mouse click
       print(x,'',y)

       #how to define or print on same window
       font = cv.FONT_HERSHEY_PLAIN
       cv.putText(img, str(x) + ','+ str(y), (x,y), font, 1, (255,0,0), thickness=2)

       #text show on image
       cv.imshow("image", img)
# for color finding
    if event == cv.EVENT_RBUTTONDOWN:
        print(x, '', y)

        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]

        cv.putText(img, str(b) + ','+ str(g) + ','+ str(r), (x,y), font, 1, (28,64,40), 2)
        cv.imshow('image', img)

#final funtion to read and display
if __name__=="__main__":
    #reading an image
    img=cv.imread("download.png", 1)
    #display the image
    cv.imshow('image', img)
    #set mouse (callback function)
    cv.setMouseCallback("image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()