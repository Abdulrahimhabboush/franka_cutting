cmake_minimum_required(VERSION 3.0.2)
project(franka_cutting)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})


catkin_install_python(
  PROGRAMS scripts/move_to_start.py scripts/test.py scripts/test_joint.py scripts/plan_cartesian_path.py scripts/choping.py scripts/sawing.py scripts/pressing_and_slicing.py scripts/current_pose.py scripts/chopping.py scripts/slicing.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
