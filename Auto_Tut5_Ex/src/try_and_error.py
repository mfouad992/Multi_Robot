#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Pose


def Pub_1():
    pub = rospy.Publisher('/APF_Des_Pos', Pose, queue_size=10)
    rospy.init_node('Pose_pub', anonymous=True)
    rate = rospy.Rate(2) # Hz
    while not rospy.is_shutdown():
        p = Pose()
        p.position.x = 2.5
        p.position.y = 4.5
        p.position.z = 1.0
        # Make sure the quaternion is valid and normalized
        p.orientation.x = 0.0
        p.orientation.y = 0.0
        p.orientation.z = 0.0
        p.orientation.w = 1.0
        pub.publish(p)
        rate.sleep()

if __name__ == '__main__':
    try:
        Pub_1()
    except rospy.ROSInterruptException:
        pass
