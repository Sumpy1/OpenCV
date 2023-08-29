import numpy as np
import cv2 as cv

img = cv.imread('Photos/fisk.jpeg')
cv.imshow("fisk",img)

#Translate
def translate(img,x,y):
    transMat=  np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


#-x -->left
#-y -->up
#x -->right
#y --> down

translated = translate(img,-100,-100)
cv.imshow('translated',translated)

#Rotation
def rotation(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)
        rotMat= cv.getRotationMatrix2D(rotpoint,angle,1.0)
        dimensions= (width,height)
        return cv.warpAffine(img,rotMat,dimensions)


rotated=rotation(img,90)
cv.imshow('rotated',rotated)

#Resizing
resize= cv.resize(rotated,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized rotated',resize)


cv.waitKey(0)
