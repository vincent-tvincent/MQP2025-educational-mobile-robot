# from  actuator_package.servo_group import port_init, port_open, port_close
from actuator_package import *
from actuator_package.servo_port_handler import *
from chassis_drive import chassis_4wdiff
from gimbal_drive import gimbal_yaw_pitch
import time
import math

portHandler = port_init('/dev/ttyUSB0', 115200)

port_open(portHandler)
  # Adjust the device name as needed
chassis = chassis_4wdiff(portHandler)
gimbal = gimbal_yaw_pitch(portHandler) 
# chassis.wheel_zeroing()
# chassis.enable_torque()
# print(chassis.read_feedback_4wdiff())
# time.sleep(1)
# print(chassis.set_speed_4wdiff([0, 0.25 * math.pi]))  # Set linear speed to 100 mm/s and angular speed to 0 rad/s
# print(chassis.read_feedback_4wdiff())

# for i in range(20):
#     print(chassis.read_feedback_4wdiff())
#     time.sleep(0.1)

# print(chassis.set_speed_4wdiff([0, 0]))  # Set linear speed to 0 mm/s and angular speed to 1 rad/s
# chassis.disable_torque()
gimbal.gimbal_zeroing()
time.sleep(0.5)
gimbal.disable_torque()

port_close(portHandler)

