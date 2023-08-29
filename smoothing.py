import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img= cv.imread('Photos/sos.jpeg')
cv.imshow('Sos',img)

#Averaging blur method
average=cv.blur(img,(3,3))
cv.imshow('Average blur',average)

#Gaussian blur
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

#Median blur
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)

#Bilateral blurring
bilateral=cv.bilateralFilter(img,10,15,15)
cv.imshow('Bilateral blurring',bilateral)


cv.waitKey(0)