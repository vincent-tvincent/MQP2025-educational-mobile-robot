from setuptools import find_packages, setup

package_name = 'robot_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(
        exclude=['test']
    ),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch_control.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bluelobster',
    maintainer_email='bluelobster@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'gimbal_control = robot_control.gimbal_control:main',
            'chassis_control = robot_control.chassis_control:main',
            'imu_processing = robot_control.imu_processing:main',
            'lidar_processing = robot_control.lidar_processing:main',
            'imu_test_plot = robot_control.imu_test_plot:main',
            'odometry_generator = robot_control.odometry_generator:main',
            'joystick_input = robot_control.joystick_input:main',
            'robot_map = robot_control.robot_map:main'
        ],
    },
)
