from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
def generate_launch_description():
    return LaunchDescription([ 
        DeclareLaunchArgument('serial_port', default_value='/dev/ttyUSB1',description='the serial port for dynamixel controller'),
        Node(
            package='actuator_nodes',
            executable='actuation_node',
            name='actuation_node',
            output='screen',
            parameters=[{
                'serial_port': LaunchConfiguration('serial_port'), 
            }]
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
