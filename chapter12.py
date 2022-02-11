# setting of camera or vdo
import cv2 as cv
import numpy as np

cap= cv.VideoCapture(0)

cap.set(10, 50)#10  is the key to set brightness
cap.set(3, 640) #width
cap.set(4, 480) #height
while (True):
    ret, frame = cap.read()
    if ret ==True:
        cv.imshow("frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()