#!/usr/bin/env python
# This is the lib which will be used alongside with ros to interface with the car_libs
# Structure of the code will be
# there will be a subscriber and a publisher
# subscriber will subsribe to the acceleration or throttle value of the car
# publisher will publish the velocity on a top from 0 - 100 or whatever value we require
# this will just act as interface
# we can also subscribe to the distance of the cat
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import Float32
from sample_rc_throt import car
from time import sleep


def throtCb(data):
    dagu.throttle(data.data)
    sleep(0.1)
    dagu.throttle(0)



dagu = car()
rospy.init_node('Car')
pub = rospy.Publisher('vel',Float32, queue_size = 10)
sub = rospy.Subscriber('thort',Int32, throtCb)
rate = rospy.Rate(10) # 10 Hz
rospy.spin()
while not rospy.is_shutdown():

    pub.publish()
