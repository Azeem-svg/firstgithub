# converting a video into gray or blacj and white
import cv2 as cv
cap= cv.VideoCapture('vdi.mp4')
# writing format, codec, video writer object and file outpput
frame_width= int(cap.get(3))
frame_height= int(cap.get(4))
out= cv.VideoWriter('outvid.avi', cv.VideoWriter_fourcc('M','J','P','G'),10,(frame_width, frame_height), isColor=False)

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
#to show in a player
    if ret == True:
        out.write(grayframe)   
        cv.imshow('vdi', grayframe)#changing name gray ,gray rame or binary will change the video
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()