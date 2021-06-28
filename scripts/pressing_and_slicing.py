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
#intial pose
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.3239551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)   

#pose 2
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.3039551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 3
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.2839551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 4
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.2639551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 5
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.2439551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 6
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.2239551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 7
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.2039551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 8
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.1839551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 9
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.1639551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 10
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.14139551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 11
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.1239551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 12
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.1039551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 13
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.0739551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 14
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.0539551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 15
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.0339551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 16
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.0139551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 17
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 0.9939551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#pose 18
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 0.9739551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#the cutting board pose 1
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 0.9738522035073995

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#the cutting board pose 2
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 0.9638522035073995

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#the cutting board pose 3
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9165375936731941
pose_goal.orientation.y = -0.3890361848918819
pose_goal.orientation.z = 0.03231359448453804
pose_goal.orientation.w = 0.08697998528402608

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.2159773466236021
pose_goal.position.z = 0.9725873931977209

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)

#Initial pose
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875
pose_goal.orientation.y = -0.38053784482433245
pose_goal.orientation.z = 0.013179018537871666
pose_goal.orientation.w = 0.04829052491278604

pose_goal.position.x = 0.6164381313722648
pose_goal.position.y = -0.10587658432225745
pose_goal.position.z = 1.3239551617867288

move_group.set_pose_target(pose_goal)
plan = move_group.go(wait=True)  

#taking the picture after cutting
capture_service()  
rospy.sleep(5)
    
moveit_commander.roscpp_shutdown()
