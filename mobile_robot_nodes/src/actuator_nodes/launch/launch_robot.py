from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='actuator_nodes',
            executable='actuation_node',
            name='actuation_node',
            output='screen'
        ),
        # Node(
        #     package='computer_vision_nodes',
        #     executable='your_cv_executable',
        #     name='vision_node',
        #     output='screen'
        # ),
        Node(
            package='localization_nodes',
            executable='imu_node',
            name='imu_node',
            output='screen'
        ),
    ])
