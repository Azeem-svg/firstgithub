
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
hd_resolution()

while (True):
    ret, frame = cap.read()
    if ret ==True:
        cv.imshow("camera", frame)
        cv.imshow("came", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()