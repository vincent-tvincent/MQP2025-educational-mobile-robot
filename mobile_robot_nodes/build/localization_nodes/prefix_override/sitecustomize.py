import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pipi/ros2_projects/workspaces/mobile_robot/mobile_robot_nodes/install/localization_nodes'
