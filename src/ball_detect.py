

#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
import cv2
import numpy as np
import rospy, time
from copy import deepcopy
from tf.transformations import quaternion_from_euler
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class Shefali():
    def __init__(self):
        self.bridge_object = CvBridge()
        rospy.init_node('latika',anonymous=True)
        rospy.Subscriber("/camera/color/image_raw", Image, self.callback)
        
    def callback(self,data):
        frame = self.bridge_object.imgmsg_to_cv2(data, desired_encoding="bgr8")
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        l_b = np.array([90, 100, 0])
        u_b = np.array([255, 170, 120])

        mask = cv2.inRange(hsv, l_b, u_b)


        image = cv2.bitwise_and(frame, frame, mask=mask)

        #image = cv2.imread('check4-res.png')
        mask = np.zeros(image.shape, dtype=np.uint8)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=5)

        cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        blobs = 0
        for c in cnts:
            area = cv2.contourArea(c)
            cv2.drawContours(mask, [c], -1, (36,255,12), -1)
            if area > 13000:
                blobs += 2
            else:
                blobs += 1

        #print('blobs:', blobs)
        pub = rospy.Publisher("blobs_publisher", Int64, queue_size=10)
        pub.publish(blobs)

        cv2.imshow('mask', mask)
        cv2.waitKey(3)


if __name__ == '__main__':
    Shefali()
    rospy.spin()