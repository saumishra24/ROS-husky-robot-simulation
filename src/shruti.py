import rospy
from std_msgs.msg import String
from std_msgs.msg import Int64
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
count = 0
sequence = list()
sum = 0
remainder =0

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

def callback(data):
    global remainder
    remainder = data.data
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()
    print(remainder)
    print(type(remainder))

    # if(remainder == 0):
    #     goal = MoveBaseGoal()
    #     goal.target_pose.header.frame_id = "map"
    #     goal.target_pose.header.stamp = rospy.Time.now()

    #     goal.target_pose.pose.position.x =  7.66735519085
    #     goal.target_pose.pose.position.y = 6.91302261313
    #     goal.target_pose.pose.position.z = 0.0
    #     goal.target_pose.pose.orientation.x = -2.66347565979e-07

    #     goal.target_pose.pose.orientation.y = 1.2343228759e-07
    #     goal.target_pose.pose.orientation.z =  0.272616634607
    #     goal.target_pose.pose.orientation.w = 0.962122741925

    #     navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    #     finished = navclient.wait_for_result() 
    
    # if(remainder == 2):
    #     print("remainder 2 hai")
    #     goal = MoveBaseGoal()
    #     goal.target_pose.header.frame_id = "map"
    #     goal.target_pose.header.stamp = rospy.Time.now()

    #     goal.target_pose.pose.position.x = 8.03285174022
    #     goal.target_pose.pose.position.y = 5.38854316613
    #     goal.target_pose.pose.position.z = 0.0
    #     goal.target_pose.pose.orientation.x = -2.1955152363e-06

    #     goal.target_pose.pose.orientation.y =  -2.08303261298e-06
    #     goal.target_pose.pose.orientation.z =  0.270254981586
    #     goal.target_pose.pose.orientation.w =  0.962788785206

    #     navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    #     finished = navclient.wait_for_result()
    
    # if(remainder == 3):
    #     goal = MoveBaseGoal()
    #     goal.target_pose.header.frame_id = "map"
    #     goal.target_pose.header.stamp = rospy.Time.now()
    #     goal.target_pose.pose.position.x = 9.56917687045
    #     goal.target_pose.pose.position.y =  3.08714121995
    #     goal.target_pose.pose.position.z = 0.0
    #     goal.target_pose.pose.orientation.x = -2.7362427017e-06
    #     goal.target_pose.pose.orientation.y = 7.72779200054e-07
    #     goal.target_pose.pose.orientation.z = -0.0220083631994
    #     goal.target_pose.pose.orientation.w =  0.999757786637

    #     navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    #     finished = navclient.wait_for_result()

    # if(remainder == 4):
    #     goal = MoveBaseGoal()
    #     goal.target_pose.header.frame_id = "map"
    #     goal.target_pose.header.stamp = rospy.Time.now()
    #     goal.target_pose.pose.position.x =  8.06020937829
    #     goal.target_pose.pose.position.y =  -1.79289145952
    #     goal.target_pose.pose.position.z = 0.0
    #     goal.target_pose.pose.orientation.x = 2.80366168571e-07
    #     goal.target_pose.pose.orientation.y = -5.03025972765e-07
    #     goal.target_pose.pose.orientation.z =  -0.305745052935
    #     goal.target_pose.pose.orientation.w = 0.952113418982

    #     navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    #     finished = navclient.wait_for_result()

       
    
    # if(remainder == 1):
    #     goal = MoveBaseGoal()
    #     goal.target_pose.header.frame_id = "map"
    #     goal.target_pose.header.stamp = rospy.Time.now()
    #     goal.target_pose.pose.position.x = 7.92612617918
    #     goal.target_pose.pose.position.y = 0.633009035081
    #     goal.target_pose.pose.position.z = 0.0
    #     goal.target_pose.pose.orientation.x =-1.1670445089e-07
    #     goal.target_pose.pose.orientation.y = -2.80875948699e-08
    #     goal.target_pose.pose.orientation.z = 0.304027355254
    #     goal.target_pose.pose.orientation.w = -0.952663302147
    #     navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    #     finished = navclient.wait_for_result()
    
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x =12.0742110939
    goal.target_pose.pose.position.y = 2.97727858992
    goal.target_pose.pose.position.z = 0.0
    goal.target_pose.pose.orientation.x = -8.96856512745e-08
    goal.target_pose.pose.orientation.y = 2.34346055819e-08
    goal.target_pose.pose.orientation.z = -0.0220443494203
    goal.target_pose.pose.orientation.w = 0.999756993803
    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()
    print("shefali ma'am op")
    

    if not finished:
        rospy.logerr("Action server not available!")
    else:
        rospy.loginfo ( navclient.get_result())
    


def listener():

    rospy.init_node('final_gates', anonymous=True)


    rospy.Subscriber("remainder_giver", Int64, callback)
    

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()