#!/usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from zivid_camera.srv import *

# Require zivid
try:
    rospy.wait_for_service("/zivid_camera/capture")
    rospy.sleep(5)
except rospy.ROSInterruptException:
    exit()
    
# Start capture function
capture_service = rospy.ServiceProxy("/zivid_camera/capture", Capture)

# Wait to start movement
rospy.wait_for_service("/zivid_camera/capture")
rospy.sleep(10)
rospy.wait_for_service("/zivid_camera/capture")
rospy.sleep(10)
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('test', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory,
                                                   queue_size=20)
#Initial pose
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.17587658432225745
pose_goal.position.z = 1.3239551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#Pose 2
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.17587658432225745
pose_goal.position.z = 1.0539551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#Pose 3
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.17587658432225745
pose_goal.position.z = 0.9438522035073995

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#Initial pose
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.17587658432225745
pose_goal.position.z = 1.3239551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#taking a picture after cutting
capture_service()
rospy.sleep(5)
    
moveit_commander.roscpp_shutdown()

