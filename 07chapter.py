# converting a video into gray or blacj and white
import cv2 as cv
cap= cv.VideoCapture('vdi.mp4')

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)

#to show in a player
    if ret == True:
        # cv.imshow('vdo', binary) 
        # cv.imshow('vdo', gray)
        cv.imshow('vdo', grayframe)#changing name gray ,gray rame or binary will change the video


        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()