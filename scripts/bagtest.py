#!/usr/bin/python
import rospy
import rosbag
from std_msgs.msg import Int32, String


bag = rosbag.Bag('bagtest','w')

def sub_imu(data):  
    bag.write('/imu/data',data)


rospy.init_node('bag_recorder')    
sub = rospy.Subscriber('/turtle1/cmd_vel', String, sub_imu )
rospy.spin()
bag.close()
    


#Set up message from String
s = String()
s.data = 'foo'
#Set up message from Int32
i = Int32()
i.data = 42

bag.write('chatter', s)
bag.write('numbers', i)

bag.close()

