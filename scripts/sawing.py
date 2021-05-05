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

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.3239551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

capture_service()
rospy.sleep(5)  
   
pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0539551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0439551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0439551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0339551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0339551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)


pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0239551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0239551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0139551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0139551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)


pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0039551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.0039551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9939551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9939551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9839551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9839551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)


pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9739551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9739551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.10587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9639551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 0.9639551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x =0.9234095988944875#-0.886255420986795 #0.0
pose_goal.orientation.y = -0.38053784482433245#0.28602401015314566 #0.0
pose_goal.orientation.z = 0.013179018537871666#-0.36398034203008306 #0.0
pose_goal.orientation.w = 0.04829052491278604#0.0161215694985304 #1.0

pose_goal.position.x = 0.6164381313722648#0.6502561169158649 #0.4
pose_goal.position.y = -0.19587658432225745#-0.06959042110924456 #0.1
pose_goal.position.z = 1.3239551617867288#0.9743180028822862 #0.4

move_group.set_pose_target(pose_goal)
#print(move_group.get_current_pose().pose)
plan = move_group.go(wait=True)

capture_service()
rospy.sleep(5)
    
moveit_commander.roscpp_shutdown()
