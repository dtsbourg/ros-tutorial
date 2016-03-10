#!/usr/bin/env python
# encoding=utf-8
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$


import rospy
import roslib; roslib.load_manifest('beginner_tutorials')
from std_msgs.msg import String
from geometry_msgs.msg import Pose, Point
from beginner_tutorials.msg import ScaledPose

__last_state__ = ScaledPose()
__last_string__ = "hello"

def pose_callback(data):
    global __last_state__
    __last_state__ = data

def callback(data):
    global __last_string__
    __last_string__ = data.data

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    rospy.Subscriber('pose_logger', ScaledPose, pose_callback)
    print "Subscribed"

def work_loop():
    rate = rospy.Rate(5) # 5 Hz
    while not rospy.is_shutdown():
        print "Last string : \n %s" % __last_string__
        print "Last scaled pose : "
        print scale_pose(__last_state__.pose, __last_state__.scale)
        rate.sleep()

def scale_pose(pose, scale):
    pos = pose.position
    scaled_pos = Point(pos.x * scale, pos.y * scale, pos.z * scale)
    return Pose(scaled_pos, pose.orientation)

if __name__ == '__main__':
    listener()
    work_loop()
