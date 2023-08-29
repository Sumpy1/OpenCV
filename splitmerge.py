import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('Photos/sos.jpeg')
cv.imshow('Sos',img)

#creating a blank image
blank=np.zeros(img.shape[:2],dtype='uint8')

#splitting images in b,g,r and merging them
b,g,r=cv.split(img)
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

print(img.shape)
print(b.shape)
print(r.shape)

merged= cv.merge([b,g,r])
cv.imshow('merged',merged)
cv.waitKey(0)