#!/usr/bin/env python
# encoding=utf-8

import roslib; roslib.load_manifest('beginner_tutorials')
from beginner_tutorials.srv import *
import rospy

def handle_echo(req):
    print "Returnin echo :"
    echo_string = '\n'.join([req.word] * req.echo_strength)
    print echo_string
    return EchoResponse(echo_string)

def echo_server():
    rospy.init_node('echo_server')
    s = rospy.Service('echo', Echo, handle_echo)
    rospy.spin() # Keeps code from exiting until service is shutdown

if __name__ == "__main__":
    echo_server()
