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
joint_goal[0] = 2.6349746363109627
joint_goal[1] = -0.726
joint_goal[2] = -2.772
joint_goal[3] = -1.846
joint_goal[4] = -0.6988
joint_goal[5] = 2.455
joint_goal[6] = 1.12388
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6268
joint_goal[1] = -0.7297
joint_goal[2] = -2.83225
joint_goal[3] = -1.821
joint_goal[4] = -0.69855
joint_goal[5] = 2.45657
joint_goal[6] = 1.076077
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6855
joint_goal[1] = -0.7497
joint_goal[2] = -2.832114
joint_goal[3] = -1.82079
joint_goal[4] = -0.69855
joint_goal[5] = 2.45657
joint_goal[6] = 1.2211489
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6051
joint_goal[1] = -0.766432
joint_goal[2] = -2.86582
joint_goal[3] = -1.78622
joint_goal[4] = -0.6989
joint_goal[5] = 2.50163
joint_goal[6] = 1.0258
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.7367
joint_goal[1] = -0.79833219
joint_goal[2] = -2.8636199
joint_goal[3] = -1.78759
joint_goal[4] = -0.698866
joint_goal[5] = 2.50118
joint_goal[6] = 1.181969
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6326
joint_goal[1] = -0.7999
joint_goal[2] = -2.8817
joint_goal[3] = -1.7711
joint_goal[4] = -0.6989044
joint_goal[5] = 2.50896
joint_goal[6] = 1.054227
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.7596
joint_goal[1] = -0.8309
joint_goal[2] = -2.8760
joint_goal[3] = -1.77097
joint_goal[4] = -0.6982988
joint_goal[5] = 2.5090819
joint_goal[6] = 1.187376599
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.61236
joint_goal[1] = -0.880571
joint_goal[2] = -2.891926
joint_goal[3] = -1.6890788
joint_goal[4] = -0.697785
joint_goal[5] = 2.508654
joint_goal[6] = 1.01436
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6982486
joint_goal[1] = -0.8830836
joint_goal[2] = -2.870816
joint_goal[3] = -1.728972
joint_goal[4] = -0.6959586
joint_goal[5] = 2.5079107
joint_goal[6] = 1.057312
    
plan = move_group.go(joint_goal, wait=True)


#here starts the problem
joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.60000
joint_goal[1] = -0.94892571194
joint_goal[2] = -2.889653
joint_goal[3] = -1.623959
joint_goal[4] = -0.6965
joint_goal[5] = 2.5080086
joint_goal[6] = 0.96068
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.67725566
joint_goal[1] = -0.95075
joint_goal[2] = -2.86853
joint_goal[3] = -1.6558
joint_goal[4] = -0.6964976
joint_goal[5] = 2.508017
joint_goal[6] = 1.029754
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.60907
joint_goal[1] = -0.914859
joint_goal[2] = -2.8914946
joint_goal[3] = -1.67595
joint_goal[4] = -0.69713135
joint_goal[5] = 2.508632833
joint_goal[6] = 0.999
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.70123
joint_goal[1] = -0.929583
joint_goal[2] = -2.8863499
joint_goal[3] = -1.684471
joint_goal[4] = -0.69582
joint_goal[5] = 2.50858388
joint_goal[6] = 1.0135616
    
plan = move_group.go(joint_goal, wait=True)

joint_goal = move_group.get_current_joint_values()
joint_goal[0] = 2.6555
joint_goal[1] = -0.9428466
joint_goal[2] = -2.894777
joint_goal[3] = -1.6699
joint_goal[4] = -0.6961334
joint_goal[5] = 2.50935
joint_goal[6] = 1.0064146
    
plan = move_group.go(joint_goal, wait=True)


#joint_goal = move_group.get_current_joint_values()
#joint_goal[0] = 2.6880981849546055
#joint_goal[1] = -0.908882182897984
#joint_goal[2] = -2.862393950412292
#joint_goal[3] = -1.715162442657154
#joint_goal[4] = -0.8132203487391758
#joint_goal[5] = 2.4857365463126775
#joint_goal[6] = 1.1595994568218786
    
#plan = move_group.go(joint_goal, wait=True)

   
rospy.sleep(5)
    
moveit_commander.roscpp_shutdown()
