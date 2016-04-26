#!/usr/bin/env python
# coding=utf-8

import rospy
import random
import roslib; roslib.load_manifest('beginner_tutorials')
from std_msgs.msg import String
from sys import stdin
import sys, tty, termios

def key_talker():
    pub = rospy.Publisher('key_logger', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz -- Change rate to rate of bag file
    while not rospy.is_shutdown():
	fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	pub_msg = String(ch)
        print pub_msg
        pub.publish(pub_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        key_talker()
    except rospy.ROSInterruptException:
        pass
