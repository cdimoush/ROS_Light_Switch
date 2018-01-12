#! /usr/bin/env python

from arduino_service.srv import *
from std_srvs.srv import Empty, EmptyResponse
from std_msgs.msg import Empty as empty_message
import rospy


def relay_on(arg):
    pub1 = rospy.Publisher('relay_on', empty_message, queue_size=10)
    pub1.publish()

    return EmptyResponse()


def relay_off(arg):
    pub2 = rospy.Publisher('relay_off', empty_message, queue_size=10)
    pub2.publish()

    return EmptyResponse()


def arduino_server():
    rospy.init_node('arduino_server')
    s1 = rospy.Service('lights_on', Empty, relay_on)
    s2 = rospy.Service('lights_off', Empty, relay_off)

    relay_on(Empty)  # THE ARDUINO DOEST RECEIVE MESSAGE THE FIRST TIME!!!!!
    relay_off(Empty)  # Calling the both functions initially fixes the problem

    print('Services are Ready')
    rospy.spin()


if __name__ == '__main__':
    arduino_server()


