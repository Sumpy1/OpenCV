import cv2 as cv
import numpy as np

#reading the image file
img = cv.imread('Photos/sos.jpeg')
cv.imshow("SOS",img)

#Creating blank image using numpy
blank= np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

#Converting to grayscale
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Using Gaussian blur
blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Using Canny
canny=cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#printing the number of contours
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} are found!!!')

#Drawing contours in red
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours drawn',blank)


cv.waitKey(0)