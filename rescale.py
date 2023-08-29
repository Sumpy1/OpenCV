import cv2 as cv

img = cv.imread('Desktop/OpenCV/Photos/sos.jpeg')
cv.imshow("SOS",img)

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions= (width, height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

resized_img= rescaleFrame(img)
cv.imshow('resized', resized_img)
cv.waitKey(0)

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)

    return
capture = cv.VideoCapture("Videos/mixkit-baby-on-the-belly-of-his-mother-plays-and-smiles-4042-medium.mp4")

while True:
    isTrue, frame =capture.read()
    frame_resized = rescaleFrame(frame)
    #cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()


