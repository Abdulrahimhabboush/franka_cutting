#!/usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

#rospy.wait_for_service("/zivid_camera/capture)
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('test', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)
#pose 1                                                   
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.14418
joint_goal[2] = -0.166
joint_goal[3] = -1.82311
joint_goal[4] = -0.04525
joint_goal[5] = 1.96187
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 2    
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.17824
joint_goal[2] = -0.166
joint_goal[3] = -1.869889
joint_goal[4] = -0.045
joint_goal[5] = 2.0551
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)  

#pose 3 
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.1907558
joint_goal[2] = -0.166
joint_goal[3] = -1.870346
joint_goal[4] = -0.045
joint_goal[5] = 2.0637
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True) 

#pose 4
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.22179
joint_goal[2] = -0.166
joint_goal[3] = -1.9194345
joint_goal[4] = -0.045
joint_goal[5] = 2.147
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True) 

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.237
joint_goal[2] = -0.166
joint_goal[3] = -1.958
joint_goal[4] = -0.045
joint_goal[5] = 2.2012
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True) 

#pose 6
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.289
joint_goal[2] = -0.166
joint_goal[3] = -1.9714
joint_goal[4] = -0.045
joint_goal[5] = 2.2820
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 7
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.344
joint_goal[2] = -0.166
joint_goal[3] = -1.9711
joint_goal[4] = -0.045
joint_goal[5] = 2.35
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 8
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.437
joint_goal[2] = -0.166
joint_goal[3] = -1.9712
joint_goal[4] = -0.045
joint_goal[5] = 2.45
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 9
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.4959
joint_goal[2] = -0.166
joint_goal[3] = -1.97119
joint_goal[4] = -0.045
joint_goal[5] = 2.5
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 10
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.5768
joint_goal[2] = -0.166
joint_goal[3] = -1.97114
joint_goal[4] = -0.045
joint_goal[5] = 2.6
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 11
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.67319
joint_goal[2] = -0.166
joint_goal[3] = -1.97069
joint_goal[4] = -0.045
joint_goal[5] = 2.7
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)

#pose 12
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.749
joint_goal[2] = -0.166
joint_goal[3] = -1.96228
joint_goal[4] = -0.045
joint_goal[5] = 2.75
joint_goal[6] = 0.53
    
plan = move_group.go(joint_goal, wait=True)

#pose 13
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.789
joint_goal[2] = -0.166
joint_goal[3] = -1.95
joint_goal[4] = -0.045
joint_goal[5] = 2.8
joint_goal[6] = 0.55
    
plan = move_group.go(joint_goal, wait=True)

#pose 14
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.812
joint_goal[2] = -0.166
joint_goal[3] = -1.94
joint_goal[4] = -0.045
joint_goal[5] = 2.8
joint_goal[6] = 0.55
    
plan = move_group.go(joint_goal, wait=True)

#pose 15
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.82
joint_goal[2] = -0.166
joint_goal[3] = -1.939
joint_goal[4] = -0.045
joint_goal[5] = 2.8
joint_goal[6] = 0.55
    
plan = move_group.go(joint_goal, wait=True)

#pose 16
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.835
joint_goal[2] = -0.166
joint_goal[3] = -1.937
joint_goal[4] = -0.045
joint_goal[5] = 2.83
joint_goal[6] = 0.55
    
plan = move_group.go(joint_goal, wait=True)

#pose 1                                                   
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = -0.166
joint_goal[1] = 0.14418
joint_goal[2] = -0.166
joint_goal[3] = -1.82311
joint_goal[4] = -0.04525
joint_goal[5] = 1.96187
joint_goal[6] = 0.5
    
plan = move_group.go(joint_goal, wait=True)
   
rospy.sleep(5)
    
moveit_commander.roscpp_shutdown()
