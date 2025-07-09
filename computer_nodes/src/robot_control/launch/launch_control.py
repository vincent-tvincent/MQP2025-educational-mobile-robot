from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_control',
            executable='imu_processing',
            name='imu_processing',
            output='screen'
        ),
        Node(
            package='robot_control',
            executable='chassis_control',
            name='chassis_control',
            output='screen'
        ),
    ])