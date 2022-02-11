#split your vdos into frames
import cv2 as cv

cap=cv.VideoCapture('vdi.mp4')
frameNr = 0

while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+2
cap.release()