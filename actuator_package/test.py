from robot_servo import *

port_init()

# set_torque_enable(0)
# set_torque_enable(1)
# set_mode_velocity(0)
# set_mode_velocity(1)
# set_goal(0, 0)
# set_goal(1, 0)

wheel_group = servo_group(MODE_VELOCITY, [0, 1])
wheel_group.set_torque_status(TORQUE_ENABLE)

wheel_group.set_goals([1000,1000])
time.sleep(1)
result = wheel_group.get_feedback()
print(result)
wheel_group.set_torque_status(TORQUE_DISABLE)
port_close()