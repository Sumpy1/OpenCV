import cv2 as cv

#reading the image file
img = cv.imread('Photos/sos.jpeg')
cv.imshow("SOS",img)

#converting to gray scale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur= cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#canny
canny = cv.Canny(img,125,175)
cv.imshow('Canny', canny)

#dilating the image
dilate = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilate',dilate)

#Eroded
erode= cv.erode(dilate,(3,3),iterations=1)
cv.imshow('erode',erode)

#resize
resize= cv.resize(img,(500,500),interpolation=2)
cv.imshow('resize',resize)

#Cropping
cropped= img[0:300]
cv.imshow('cropped',cropped)

#waits to exit till any key is pressed
cv.waitKey(0)
