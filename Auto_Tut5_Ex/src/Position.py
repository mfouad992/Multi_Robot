#! /usr/bin/env python2

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist,Pose

flag_initial = 0 

pos_msg_0= Pose()
Velocity_msg_0 = Twist()

def callback(data):
    msg = data
    global pos_msg_0
    global flag_initial 
    global Velocity_msg_0

    pos_msg_0.position.x = round(msg.pose.pose.position.x, 4)		#Round the value of x to 4 decimal places
    pos_msg_0.position.y = round(msg.pose.pose.position.y, 4)		#Round the value of y to 4 decimal places
    pos_msg_0.position.z = round(msg.pose.pose.position.z, 4)		#Round the value of y to 4 decimal places
    pos_msg_0.orientation.x = round(msg.pose.pose.orientation.x, 4)	#Round the value of theta to 4 decimal places
    pos_msg_0.orientation.y = round(msg.pose.pose.orientation.y, 4)	#Round the value of theta to 4 decimal places
    pos_msg_0.orientation.z = round(msg.pose.pose.orientation.z, 4)	#Round the value of theta to 4 decimal places
    pos_msg_0.orientation.w = round(msg.pose.pose.orientation.w, 4)	#Round the value of theta to 4 decimal places
    
    Velocity_msg_0.linear.x = round(msg.twist.twist.linear.x, 4)
    Velocity_msg_0.linear.y = round(msg.twist.twist.linear.y, 4)
    Velocity_msg_0.linear.z = round(msg.twist.twist.linear.z, 4)
    Velocity_msg_0.angular.x = round(msg.twist.twist.angular.x, 4)
    Velocity_msg_0.angular.y = round(msg.twist.twist.angular.y, 4)
    Velocity_msg_0.angular.z = round(msg.twist.twist.angular.z, 4)
    
    flag_initial = 1
    Pose_Sub.unregister()				#Unsubsribe from this topic

    print pos_msg_0 
    print 40*"**"
    print Velocity_msg_0 
    #print msg.pose.pose


rospy.init_node('Check_Position')
Pose_Sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()

#--------------------------------------------------------------------------------
