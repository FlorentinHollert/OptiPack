from object_detector import *
import cv2
import numpy as np

from ArucoDetection.object_detector import HomogeneousBgDetector

url = "http://172.17.30.23:8080/video"
def caputureInput():
    try:
        cap = cv2.VideoCapture(url)

        cap.set(10,160)
        cap.set(3,1920)
        cap.set(4,1080)
        #cap.set(5,25)
        # Load Aruco detector
        parameters = cv2.aruco.DetectorParameters_create()
        aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)

        measured = False

        # Load Object Detector
        detector = HomogeneousBgDetector()

        while(True):
            camera, frame = cap.read()
            if frame is not None:
                try:
                    resized = cv2.resize(frame, (1100, 520))
                    if(measured==True):
                        cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)
                        cv2.polylines(frame, [box], True, (255, 0, 0), 2)
                        cv2.putText(frame, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                        cv2.putText(frame, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                        resized = cv2.resize(frame, (1100, 520))
                        cv2.imshow("Frame", resized)

                    if(measured==False):
                        cv2.imshow("Frame", resized)
                    #contours = detector.detect_objects(frame)
                    # Get Aruco marker
                    corners, _, _ = cv2.aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

                    # Draw polygon around the marker
                    int_corners = np.int0(corners)
                    cv2.polylines(frame, int_corners, True, (0, 255, 0), 5)

                    # Aruco Perimeter
                    aruco_perimeter = cv2.arcLength(corners[0], True)

                    # Pixel to cm ratio
                    pixel_cm_ratio = aruco_perimeter / 20

                    contours, contourBiggest = detector.detect_objects(frame)
                    # Draw objects boundaries
                    for cnt in contours:
                        # Get rect
                        rect = cv2.minAreaRect(cnt)
                        (x, y), (w, h), angle = rect

                        # Get Width and Height of the Objects by applying the Ratio pixel to cm
                        object_width = w / pixel_cm_ratio
                        object_height = h / pixel_cm_ratio
                        # Display rectangle
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)

                        cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)
                        cv2.polylines(frame, [box], True, (255, 0, 0), 2)
                        cv2.putText(frame, "Width {} cm".format(round(object_width, 1)), (int(x - 100), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)
                        cv2.putText(frame, "Height {} cm".format(round(object_height, 1)), (int(x - 100), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)



                    #cv2.imshow("Image", frame)
                    resized = cv2.resize(frame, (1100, 520))
                    measured=True
                    cv2.imshow("Frame", resized)
                    #contourTrue.append(contourBiggest[0]*object_width)
                    #contourTrue.append(contourBiggest[1]*object_height)
                    #print(contourBiggest)
                    #print(len(contourBiggest))
                    #((contourBiggest[0][0][0]))
                    #print((contourBiggest[0][0][1]))
                    #print(len(contourBiggest[1]))

                except: cv2.waitKey(2)
                #measured=False 
    except KeyboardInterrupt:
        rectBig = cv2.minAreaRect(contourBiggest)
        (x, y), (w, h), angleBig = rectBig
        object_width = w / pixel_cm_ratio
        object_height = h / pixel_cm_ratio

        #contourBiggestWidth=contourBiggest[0][0][0]/pixel_cm_ratio
        #contourBiggesHeight=contourBiggest[0][0][1]/pixel_cm_ratio
        print(object_width)
        print(object_height)

        return object_width, object_height
    #object detector laden