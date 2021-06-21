#! /usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Pose

pos_msg= Pose()
Velocity_msg = Twist()

def callback(data):
    msg = data
    global pos_msg
    
    pos_msg.position.x = round(msg.pose.pose.position.x, 4)		#Round the value of x to 4 decimal places
    pos_msg.position.y = round(msg.pose.pose.position.y, 4)		#Round the value of y to 4 decimal places
    pos_msg.position.z = round(msg.pose.pose.position.z, 4)		#Round the value of y to 4 decimal places
    pos_msg.orientation.x = round(msg.pose.pose.orientation.x, 4)	#Round the value of theta to 4 decimal places
    pos_msg.orientation.y = round(msg.pose.pose.orientation.y, 4)	#Round the value of theta to 4 decimal places
    pos_msg.orientation.z = round(msg.pose.pose.orientation.z, 4)	#Round the value of theta to 4 decimal places
    pos_msg.orientation.w = round(msg.pose.pose.orientation.w, 4)	#Round the value of theta to 4 decimal places
    
    Velocity_msg.linear.x = round(msg.twist.twist.linear.x, 4)
    Velocity_msg.linear.y = round(msg.twist.twist.linear.y, 4)
    Velocity_msg.linear.z = round(msg.twist.twist.linear.z, 4)
    Velocity_msg.angular.x = round(msg.twist.twist.angular.x, 4)
    Velocity_msg.angular.y = round(msg.twist.twist.angular.y, 4)
    Velocity_msg.angular.z = round(msg.twist.twist.angular.z, 4)
    
    print pos_msg 
    print 40*"**"
    print Velocity_msg 
    #print msg.pose.pose

rospy.init_node('check_odometry')
#odom_sub = rospy.Subscriber('/odom', Odometry, callback)
sub0 = rospy.Subscriber('/APF_Des_Pos', Pose, callback) #Identify the subscriber "sub2" to subscribe topic "/turtle1/pose" of type "Pose"

rospy.spin()

#--------------------------------------------------------------------------------
