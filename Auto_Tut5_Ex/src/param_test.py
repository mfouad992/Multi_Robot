import rospy
from geometry_msgs.msg import Twist,Pose
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler 
import numpy as np
import math
import sympy as sym
from sympy import *

Goal_Pos = [rospy.get_param("~x_Goal"),rospy.get_param("~y_Goal")]
print(Goal_Pos[0])
