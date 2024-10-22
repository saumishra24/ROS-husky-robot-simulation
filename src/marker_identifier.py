import numpy as np
import cv2
import cv2.aruco as aruco
#cap = cv2.VideoCapture(0)
while True:
    frame = cv2.imread('/home/ishan/Pictures/Screenshot from 2021-10-02 02-01-34.png')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_5X5_100)
    arucoParameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=arucoParameters)
    frame = aruco.drawDetectedMarkers(frame, corners)
    cv2.imshow('Display', frame)
    print(ids)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cap.release()
cv2.destroyAllWindows()
