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

#pose_goal = geometry_msgs.msg.Pose()
#pose_goal.orientation.w = 1.0
#pose_goal.position.x = 0.4
#pose_goal.position.y = 0.1
#pose_goal.position.z = 0.4
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6112615823306538
joint_goal[1] = -0.25040594194753063
joint_goal[2] = -2.800244516891345
joint_goal[3] = -1.7585150775828406
joint_goal[4] = -0.0857717829743752
joint_goal[5] = 2.0214430522117324
joint_goal[6] = 0.6118222945302795
    
plan = move_group.go(joint_goal, wait=True)  
   
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6880981849546055
joint_goal[1] = -0.908882182897984
joint_goal[2] = -2.862393950412292
joint_goal[3] = -1.715162442657154
joint_goal[4] = -0.8132203487391758
joint_goal[5] = 2.4857365463126775
joint_goal[6] = 1.1595994568218786
    
plan = move_group.go(joint_goal, wait=True)    

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6112615823306538
joint_goal[1] = -0.25040594194753063
joint_goal[2] = -2.800244516891345
joint_goal[3] = -1.7585150775828406
joint_goal[4] = -0.0857717829743752
joint_goal[5] = 2.0214430522117324
joint_goal[6] = 0.6118222945302795
    
plan = move_group.go(joint_goal, wait=True)
   
rospy.sleep(5)
    
moveit_commander.roscpp_shutdown()
