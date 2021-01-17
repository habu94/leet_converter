#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('reed')
pub = rospy.Publisher('reed_data', Int32, queue_size=1)]
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    print("Please type a word")

if __name__ == '__main__':
