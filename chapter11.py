# writing vdos from cam
import cv2 as cv
import numpy as np
cap= cv.VideoCapture(0)
# writing format, codec, video writer object and file outpput
frame_width= int(cap.get(3))
frame_height= int(cap.get(4))
out= cv.VideoWriter('binary22.avi', cv.VideoWriter_fourcc('M','J','P','G'),50,(frame_width, frame_height), isColor=False)
# cv.VideoWriter()
# out= cv.VideoWriter('changedcv.avi', cv.VideoWriter_fourcc('M','J','P','G'),5,(frame_width, frame_height), isColor=False)
cv.VideoWriter()

while (True):
    (ret, frame) = cap.read()
    # gray_frame= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(frame, 127, 255, cv.THRESH_BINARY_INV)

    
#to show in a player
    if ret == True:
        # out.write(gray_frame)   
        out.write(binary) 
        # cv.imshow('vdi', frame)
        cv.imshow('qw', binary)#changing name gray ,gray rame or binary will change the video
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()