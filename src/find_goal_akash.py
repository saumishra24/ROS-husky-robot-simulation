#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
count = 0
sequence = []
sum = 0
remainder = 0
pub = rospy.Publisher("remainder_giver",Int64,queue_size=10)

def callback(data):
    global count
    global sum
    global remainder
    global sequence
    sequence.append(count)
    print(count)
    print("length hai",len(sequence))
    if(len(sequence)==3):
        for i in range(3):
            sum = sum + sequence[i]
        remainder = sum%5
        print("sum hai",sum)
        print("remainder hai abhi",remainder)
        pub.publish(remainder)


def callback2(data):
    global count
    count = data.data

def listener():

    rospy.init_node('listener3', anonymous=True)


    rospy.Subscriber("reached_goal_publisher", String, callback)
    rospy.Subscriber("blobs_publisher", Int64, callback2)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    