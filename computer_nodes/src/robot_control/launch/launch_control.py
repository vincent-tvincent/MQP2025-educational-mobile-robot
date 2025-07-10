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
        Node(
            package='robot_control',
            executable='gimbal_control',
            name='gimbal_control',
            output='screen'
        ),
        Node(
            package='robot_control',
            executable='odometry_generator',
            name='odometry_generator',
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher',
            arguments=[
                '0', '0', '0',      # x y z translation
                '0', '0', '0',      # roll pitch yaw (Euler angles)
                'odom',             # parent frame
                'base_link'         # child frame
            ],
            output='screen',
        )
    ])