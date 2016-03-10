#!/usr/bin/env python
# coding=utf-8

import rospy
import random
import roslib; roslib.load_manifest('beginner_tutorials')
from geometry_msgs.msg import Pose, Point, Quaternion
from beginner_tutorials.msg import ScaledPose

def pose_talker():
    pub = rospy.Publisher('pose_logger', ScaledPose, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        pt = Point(random.random(), random.random(), random.random())
        qt = Quaternion(random.random(),random.random(),random.random(),random.random())
        # pt = Point(1,1,1)
        # qt = Quaternion(0,0,0,0.5)
        pose = Pose(pt,qt)
        scale = random.random() * 100

        pub_msg = ScaledPose(pose, scale)
        print pub_msg
        pub.publish(pub_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        pose_talker()
    except rospy.ROSInterruptException:
        pass
