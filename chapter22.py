# face detecion in images
import cv2 as cv

#creating cascade
face_cascade = cv.CascadeClassifier('hsfd.xml')
img= cv.imread('do.jpg')
# img=cv.resize(img,(591,600))
gray_img =cv.cvtColor(img, cv.COLOR_BGR2GRAY)



faces = face_cascade.detectMultiScale(gray_img,1.1,4)
#draw a rectangle
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y), (x+w, y+h), (255,0,0),2)



#detecting phase
#




cv.imshow('image', img)
cv.imwrite('yu.png', img)
cv.waitKey(0)
cv.destroyAllWindows()