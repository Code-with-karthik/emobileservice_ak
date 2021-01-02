"""
To open front camera
"""
from cv2 import cv2

vid = cv2.VideoCapture(0)

cv2.namedWindow("test")
IMAGECOUNTER = 0

while True:
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing")
        break
    elif k%256 == 32:
        IMAGENAME = "opencv_frame_{}.png".format(IMAGECOUNTER)
        cv2.imwrite(IMAGENAME, frame)
        print("{} written!".format(IMAGENAME))
        IMAGECOUNTER += 1

vid.release()
cv2.destroyAllWindows()
