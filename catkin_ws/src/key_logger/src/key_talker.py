#!/usr/bin/env python
# coding=utf-8

import rospy
import random
from std_msgs.msg import String
from sys import stdin
import sys, tty, termios
import threading


class BgPub():
    def __init__(self, publisher):
	self.last_msg = ""
	self.publisher = publisher
	thread = threading.Thread(target=self.pub, args=self.last_msg)
	thread.daemon = True
	thread.start()

    def pub(self):
	rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.publisher.publish(self.last_msg)
	    rate.sleep()

def key_talker():
    pub = rospy.Publisher('key_logger', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    bgpub = BgPub(pub)
    rate = rospy.Rate(20) 
    while not rospy.is_shutdown():
	fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	pub_msg = String(ch)
	bgpub.last_msg = pub_msg
        rate.sleep()

if __name__ == '__main__':
    try:
        key_talker()
    except rospy.ROSInterruptException:
        pass
