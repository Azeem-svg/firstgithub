# how to detect specific color in pythn  and manage to select specific object
import cv2 as cv
import numpy as np

# img=cv.imread('frames/frame_76.jpg')

#convert into hsv(hue,saturatiion,value)
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#defining slider(hue,saturation, values etc)
def slider():
     pass
path = 'frames/frame_76.jpg'

cv.namedWindow('bars')
cv.resizeWindow('bars', 900,300)
#creating track bar

cv.createTrackbar("hue min", 'bars', 0,179, slider)
cv.createTrackbar("hue max", 'bars', 179,179, slider)
cv.createTrackbar("sat min", 'bars', 0,255, slider)
cv.createTrackbar("sat max", 'bars', 255,255, slider)
cv.createTrackbar("val min", 'bars', 0,255, slider)
cv.createTrackbar("val max", 'bars', 255,255, slider)

# how to write img
img= cv.imread(path)
# converting to hsv
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#taking values with slider

# hue_min = cv.getTrackbarPos('hue min', 'bars')
# print(hue_min)  #resolving error

#making loop
while True:
    img=cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos('hue min', 'bars')
    hue_max = cv.getTrackbarPos('hue max', 'bars')
    sat_min = cv.getTrackbarPos('sat min', 'bars')
    sat_max = cv.getTrackbarPos('sat max', 'bars')
    val_min = cv.getTrackbarPos('val min', 'bars')
    val_max = cv.getTrackbarPos('val max', 'bars')

    print(hue_min,hue_max,sat_min,sat_max, val_min, val_max)

    #to see these changes in image
    lower = np.array([hue_min,sat_min,val_min])
    upper = np.array([hue_max,sat_max,val_max])
    #masking the image
    mask_img= cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img,img, mask=mask_img)

    # cv.imshow('original', img)
    # cv.imshow('hsv', hsv_img)
    cv.imshow('mask', mask_img)
    cv.imshow('fouut', out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break
cv.destroyAllWindows()



# cv.imshow('original', img)
# cv.imshow('hsv', hsv_img)
# cv.waitKey(0)
# cv.destroyAllWindows()