import cv2 as cv
import numpy as np

#creating blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)

#paint the image a certain color
blank[0:250, 400:500] = 0,255,255
cv.imshow('green',blank)

#paint a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,255,255),thickness=cv.FILLED)
cv.imshow('Just giving the name to tab',blank)

#Draw a circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),40,(0,255,255),thickness=3)
cv.imshow('Circle',blank)

#Draw a line
cv.line(blank,(100,250),(300,400), (0,255,0),thickness=3)
cv.imshow('Line',blank)


# Write a text
cv.putText(blank,'Hello I am sumiran ',(0,255),cv.FONT_ITALIC,1.0,(0,255,0),thickness=2)
cv.imshow('text',blank)

cv.waitKey(0)



