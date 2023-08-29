import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('Photos/sos.jpeg')
cv.imshow('Sos',img)


gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to LAB
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('colored',rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)