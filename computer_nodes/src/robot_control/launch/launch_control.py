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
            executable='lidar_processing',
            name='lidar_processing',
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
            package='robot_control',
            executable='robot_map',
            output='screen'
        ), 
        Node(
            package='robot_control',
            executable='joystick_input',
            name='joystick_input',
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_chassis',
            arguments=[
                '0', '0', '0',      # x y z translation
                '0', '0', '0',     #yaw pitch roll
                'odom',             # parent frame
                'base_link'         # child frame
            ],
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_chassis',
            arguments=[
                '0', '0', '0',      # x y z translation
                '0', '0', '0',     #yaw pitch roll
                'odom',             # parent frame
                'map'         # child frame
            ],
            output='screen'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_lidar',
            arguments=[
                '0', '0', '0.2',      # x y z translation
                '0', '0', '0',        #yaw pitch roll
                'base_link',             # parent frame
                'robot_lidar'         # child frame
            ],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])