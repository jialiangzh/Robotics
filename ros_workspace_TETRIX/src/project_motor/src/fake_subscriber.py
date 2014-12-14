#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String

def listener():

    rospy.init_node('control_listener', anonymous=True)
    rospy.Subscriber('trajectory', String, callback)
    rospy.spin()

def callback(message):
	print(message.data)

if __name__ == '__main__':
	listener()