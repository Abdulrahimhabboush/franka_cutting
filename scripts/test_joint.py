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
joint_goal[0] = 2.5501906043981304
joint_goal[1] = -0.549921849508516
joint_goal[2] = -2.7172766789218836
joint_goal[3] = -1.841978177773325
joint_goal[4] = -0.4506712526215447
joint_goal[5] = 2.3005812881136922
joint_goal[6] = 0.8481238549302021
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.7087769714530667
joint_goal[1] = -0.7942696271946554
joint_goal[2] = -2.890824880265351
joint_goal[3] = -1.7179991833169272
joint_goal[4] = -0.7495143499076367
joint_goal[5] = 2.3961443152704063
joint_goal[6] = 1.0859739798637449
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.747617028424614
joint_goal[1] = -0.831971981297205
joint_goal[2] = -2.894469586590345
joint_goal[3] = -1.7217939968788118
joint_goal[4] = -0.8191143176493686
joint_goal[5] = 2.3318593151569447
joint_goal[6] = 1.2001740337759257
    
plan = move_group.go(joint_goal, wait=True)
   
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.631302747764037
joint_goal[1] = -0.896662798818391
joint_goal[2] = -2.865485479283396
joint_goal[3] = -1.7002774365868614
joint_goal[4] = -0.7877540554735396
joint_goal[5] = 2.465188562030045
joint_goal[6] = 1.0901709041347107
    
plan = move_group.go(joint_goal, wait=True)   
   
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6449656811350564
joint_goal[1] = -0.9077073808863827
joint_goal[2] = -2.873476416089009
joint_goal[3] = -1.7014048962884532
joint_goal[4] = -0.7764727097069598
joint_goal[5] = 2.4379884178636244
joint_goal[6] = 1.131359509755153
    
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
