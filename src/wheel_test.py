# from  actuator_package.servo_group import port_init, port_open, port_close
from actuator_package.robot_constant import *
from actuator_package.servo_port_handler import *
from localization_package.lidar_driver import *
from localization_package.imu_driver import *
from chassis_drive import chassis_4wdiff
from gimbal_drive import gimbal_yaw_pitch
import time
import math

# portHandler = port_init(DEVICENAME, BAUDRATE)

# port_open(portHandler)
  # Adjust the device name as needed

# imu = imu_icm20948_qwiic()
# for i in range(1):
# 	print(i)
# 	imu.caliberation()

# while(True):
# 	imu.update_imu()
# 	print(imu.read_imu())
# 	time.sleep(1)

lidar = lidar_c1()



# chassis = chassis_4wdiff(portHandler)
# gimbal = gimbal_yaw_pitch(portHandler) 
# # chassis.wheel_zeroing()
# chassis.enable_torque()
# print(chassis.read_feedback_4wdiff())
# time.sleep(1)
# # print(chassis.set_speed_4wdiff([0, 0.25 * math.pi]))  # Set linear speed to 100 mm/s and angular speed to 0 rad/s
# print(chassis.read_feedback_4wdiff())

# # for i in range(20):
# #     print(chassis.read_feedback_4wdiff())
# #     time.sleep(0.1)

# print(chassis.set_speed_4wdiff([0, 0]))  # Set linear speed to 0 mm/s and angular speed to 1 rad/s
# chassis.disable_torque()
# gimbal.gimbal_zeroing()
# time.sleep(0.5)
# gimbal.gimbal_look_down()
# time.sleep(0.5)
# gimbal.set_gimbal_position([0, 0])
# time.sleep(0.5)

# yaw = 0
# pitch = 0
# step = math.pi / 180
# for i in range(180):
# 	yaw += step
# 	pitch += step
# 	gimbal.set_gimbal_position([yaw, pitch])
# 	print(gimbal.read_feedback_gimbal())
  
# gimbal.disable_torque()
# port_close(portHandler)

