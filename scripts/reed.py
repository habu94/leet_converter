#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

rospy.init_node('reed')
pub = rospy.Publisher('reed_data', String, queue_size=10)
rate = rospy.Rate(10)

i = 0

while not rospy.is_shutdown():
    word = input(r"変換したい文字列を入力: ") #文字列を取得
    pub.publish(word)
    rate.sleep()
