#!/usr/bin/env python
# encoding=utf-8
import sys
import roslib; roslib.load_manifest('beginner_tutorials')
from beginner_tutorials.srv import *
import rospy

def echo_client(word, echo_strength):
    rospy.wait_for_service('echo')
    try:
        echo = rospy.ServiceProxy('echo', Echo)
        resp = echo(word, echo_strength)
        return resp.echo
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def usage():
    return "%s [word echo_strength] \
            - word : word to repeat \
            - echo_strength : times it will be repeated"

if __name__ == "__main__":
    if len(sys.argv) == 3:
        word = str(sys.argv[1])
        echo_strength = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)

    print "Requesting \" %s \" to be repeated %i times" % (word, echo_strength)
    print "%s" % echo_client(word, echo_strength)
