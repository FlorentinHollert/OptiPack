from email import utils
import cv2
import numpy as np
import utilities
url = "http://172.17.30.23:8080/video"
cap = cv2.VideoCapture(url)
while(True):
    camera, frame = cap.read()
    if frame is not None:
        resized = cv2.resize(frame, (600,400))
        utilities.getContours(frame, showCanny=True, )
        #cv2.imshow("Frame", resized)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()