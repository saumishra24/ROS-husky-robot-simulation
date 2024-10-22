ROS NAVIGATION :
•	Ros navigation package



OPEN CV :
Main Module Packages :
•	opencv-python 
•	opencv-contrib-python
•	opencv-python-headless
•	opencv-contrib-python-headless

Import Packages
•	import cv2
•	import numpy as np



TO RUN THE WORLD :
roslaunch takshak world1.launch
roslaunch takshak amcl_demo.launch
ball_detect.py (to find masks of the balls and publish them)
find_goal_akash.py  (to calculate remainder)
pose.py (run this only when amcl_demo shows “odom received;”)
goal_set.py (to navigate to set points)
gate_find.py (to navigate through the required gate)

 
 
TO VISUALIZE RVIZ :
visualise_rviz.rviz 