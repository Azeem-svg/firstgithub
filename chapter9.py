# how to captire a web cam inside a python
# step 1 import libraries
import cv2 as cv
import numpy as np

# step 2 readthe frames of camera 
cap=cv.VideoCapture(0) # webcame number 1,1=2 and so on
if (cap.isOpened()==False):
    print('There is an error')

# step 3 dispaly frame by frame
# read this cam untill the end
while (cap.isOpened()):
    # capture frame by frame
    ret, frame= cap.read()
    if ret==True:
        # to dispaly frames
        cv.imshow('Frame', frame)
        # to quit with q key
        if cv.waitkey(0) & 0xFF == ord('q'):
            break
    else:
        break

#step 4 release or close windows easily
cap.release()
cv.destroyAllWindows()