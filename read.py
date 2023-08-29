import cv2 as cv

#Reading the image
img = cv.imread('Photos/sos.jpeg')
cv.imshow("SOS",img)
cv.waitKey(0)

#Reading a video frame by frame
capture = cv.VideoCapture("Videos/mixkit-baby-on-the-belly-of-his-mother-plays-and-smiles-4042-medium.mp4")

while True:
    isTrue, frame =capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()


