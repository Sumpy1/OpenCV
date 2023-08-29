import cv2 as cv
import  numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/sos.jpeg')
cv.imshow('SOS',img)

blank = np.zeros(img.shape[:2],dtype='uint8')

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

circle = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask= cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask',mask)

#
# #grayscale histogram
# gray_histogram = cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('Gray histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_histogram)
# plt.xlim([0,256])
# plt.show()

#Colored pic histogram
plt.figure()
plt.title('Colored histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors= ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)