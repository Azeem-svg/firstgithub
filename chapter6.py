# reading a video
import cv2 as cv
cap= cv.VideoCapture('vdi.mp4')
#color converting a video
# cap = cv.cvtColor(cap, cv.COLOR_BGR2GRAY)
# not working
# indicator

if (cap.isOpened()==False):
    print('error in reading vdieo')

    # reading and playing
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('vdo', frame)
        if cv.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()