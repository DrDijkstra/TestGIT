import cv2
import numpy as np

cam=cv2.VideoCapture(0)

while True:
    camera,ret=cam.read()
    cv2.imshow("frame",frame)
    if(cv2.waitkey(1)==ord('q'))
        break
cam.release()
