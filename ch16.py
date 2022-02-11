# saving hd recording of cam streaming
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
# resolution
cap.set(3, 1280)
cap.set(4, 720)
# converting resolution into function
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
def sd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)
sd_resolution()     #how to change and fix the frame rate to 30frps 
# hd_resolution()



# writing format, codec, video writer object and file outpput
frame_width= int(cap.get(3))
frame_height= int(cap.get(4))
out= cv.VideoWriter('out.avi', cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width, frame_height))
# cv.VideoWriter()

while (True):
    (ret, frame) = cap.read()
    
#to show in a player
    if ret == True:
        out.write(frame)   
        cv.imshow('vdi',frame)#changing name gray ,gray rame or binary will change the video
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()