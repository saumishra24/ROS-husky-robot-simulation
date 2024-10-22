#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String

global count1

# Callbacks definition

def active_cb(extra):
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    rospy.loginfo("Current location: "+str(feedback))

def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")
    

rospy.init_node('send_goal')

pub = rospy.Publisher("reached_goal_publisher",String,queue_size=10)
navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
navclient.wait_for_server()

# Example of navigation goal

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()

goal.target_pose.pose.position.x = 7.48543757392
goal.target_pose.pose.position.y = -4.80000969941
goal.target_pose.pose.position.z = 2.70574385866e-06
goal.target_pose.pose.orientation.x =  -4.477662864e-06
goal.target_pose.pose.orientation.y = 4.62088867841e-06
goal.target_pose.pose.orientation.z = 0.97762864575
goal.target_pose.pose.orientation.w = 0.210338372552

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished = navclient.wait_for_result()
pub.publish("ubuntu")

goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "map"
goal.target_pose.header.stamp = rospy.Time.now()

goal.target_pose.pose.position.x =  -2.55467274954
goal.target_pose.pose.position.y =   -6.83605344947
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x =-1.07359453846e-05
goal.target_pose.pose.orientation.y =  -3.50877657418e-06
goal.target_pose.pose.orientation.z = 0.823129557842
goal.target_pose.pose.orientation.w =  0.567853617475

navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished = navclient.wait_for_result()
pub.publish("ubuntu")
rospy.sleep(0.2)

goal.target_pose.pose.position.x = 3.64879841115
goal.target_pose.pose.position.y = 1.65868040169
goal.target_pose.pose.position.z = 0.0
goal.target_pose.pose.orientation.x = 2.59218726719e-07
goal.target_pose.pose.orientation.y = 5.61394210543e-08
goal.target_pose.pose.orientation.z = 0.5680613824
goal.target_pose.pose.orientation.w =  0.82298618811


navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
finished = navclient.wait_for_result()
pub.publish("ubuntu")
rospy.sleep(0.2)

# goal.target_pose.pose.position.x =  8.72185683117
# goal.target_pose.pose.position.y =  7.83049487971
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = -2.66347565979e-07
# goal.target_pose.pose.orientation.y = 1.2343228759e-07
# goal.target_pose.pose.orientation.z = 0.369897364226
# goal.target_pose.pose.orientation.w = 0.929072623608


# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()
# pub.publish("ubuntu")
# rospy.sleep(0.2) 

# goal.target_pose.pose.position.x =12.0742110939
# goal.target_pose.pose.position.y = 2.97727858992
# goal.target_pose.pose.position.z = 0.0
# goal.target_pose.pose.orientation.x = -8.96856512745e-08
# goal.target_pose.pose.orientation.y = 2.34346055819e-08
# goal.target_pose.pose.orientation.z = -0.0220443494203
# goal.target_pose.pose.orientation.w = 0.999756993803


# navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
# finished = navclient.wait_for_result()
# print("shefali ma'am op")
# pub2 = rospy.Publisher("final_balls",String,queue_size=10)
# pub2.publish("finished")




if not finished:
    rospy.logerr("Action server not available!")
else:
    rospy.loginfo ( navclient.get_result())
