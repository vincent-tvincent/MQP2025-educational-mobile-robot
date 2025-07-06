import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/bluelobster/ros2_projects/workspaces/MQP2025-educational-mobile-robot/computer_nodes/install/robot_control'
