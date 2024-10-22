import rospy
from std_msgs.msg import String
from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped


rospy.init_node('pub_initial_pose',anonymous=True)
pub = rospy.Publisher('/initialpose',PoseWithCovarianceStamped ,queue_size=10)
msg = PoseWithCovarianceStamped()
msg.header.frame_id = "map"
msg.pose.pose.position.x = 11.4999574071
msg.pose.pose.position.y = -6.19858236187
msg.pose.pose.position.z = 0.0
msg.pose.pose.orientation.x = -3.88703043719e-06
msg.pose.pose.orientation.y = -4.89493381024e-07
msg.pose.pose.orientation.w = 0.00065508027158
msg.pose.pose.orientation.z = 0.999999785427


ctrl = False
rate = rospy.Rate(1)

while not ctrl:
    connectons = pub.get_num_connections()
    if(connectons>0):
        pub.publish(msg)
        ctrl = True
        print ("Kardiya")
    else:
        rate.sleep()








