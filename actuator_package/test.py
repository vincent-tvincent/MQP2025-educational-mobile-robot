from robot_servo import *

port_init()

# set_torque_enable(0)
# set_torque_enable(1)
# set_mode_velocity(0)
# set_mode_velocity(1)
# set_goal(0, 0)
# set_goal(1, 0)

delay = 0.01

gimbal_group = servo_group(MODE_POSITION, [0, 1])
wheel_group = servo_group(MODE_VELOCITY, [2, 4, 3, 5])
gimbal_group.set_torque_status(TORQUE_ENABLE)


wheel_group.set_torque_status(TORQUE_DISABLE)
# time.sleep(delay)
wheel_group.set_mode(MODE_POSITION)
wheel_group.set_torque_status(TORQUE_ENABLE)
wheel_group.set_goals([0, 0, 0, 0])
time.sleep(1)

wheel_group.set_torque_status(TORQUE_DISABLE)
#time.sleep(delay)
wheel_group.set_mode(MODE_VELOCITY)
wheel_group.set_torque_status(TORQUE_ENABLE)
#time.sleep(delay)

result1 = gimbal_group.set_goals_with_feedback([2000,2000])
result2 =wheel_group.set_goals_with_feedback([10, 10, 10, 10])
#time.sleep(delay)
result3 = gimbal_group.set_goals_with_feedback([1000,1000])
time.sleep(1)
result4 = gimbal_group.set_goals_with_feedback([2000,2000])
time.sleep(2)
result5 = wheel_group.set_goals_with_feedback([0, 0, 0, 0])

result6 = gimbal_group.get_feedback()
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
gimbal_group.set_torque_status(TORQUE_DISABLE)
#time.sleep(delay)
wheel_group.set_torque_status(TORQUE_DISABLE)
#time.sleep(delay)
port_close()
